"""
DDD 领域模型核心 - 纯净 Python，零框架依赖
包含：胜平负赔率值对象、时序位移值对象、单场比赛心电图聚合根实体
"""
from dataclasses import dataclass
from typing import Tuple, Optional
from math import isfinite


@dataclass(frozen=True)
class 赔率数值:
    """值对象：不可变的胜平负数值"""
    主胜: float
    平局: float
    客胜: float

    def __post_init__(self):
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not isfinite(v) or v <= 1
               for v in (self.主胜, self.平局, self.客胜)):
            raise ValueError("十进制赔率必须是大于1的有限数值")

    def 去水公平概率(self) -> Tuple[float, float, float]:
        """倒数比例归一化的市场隐含概率；不是 Shin，也不代表真实概率。"""
        倒数主 = 1.0 / self.主胜
        倒数平 = 1.0 / self.平局
        倒数客 = 1.0 / self.客胜
        抽水率 = (倒数主 + 倒数平 + 倒数客) - 1.0
        归一因子 = 1.0 + 抽水率
        return (倒数主 / 归一因子, 倒数平 / 归一因子, 倒数客 / 归一因子)


@dataclass(frozen=True)
class 赔率位移:
    """值对象：两点之间的位移量与变盘加速度"""
    平赔变动值: float
    每小时变盘速率: float
    异动信号: str

    def 是否显著防守降水(self, 提醒阈值: float = 0.15) -> bool:
        """旧接口名兼容：仅是可调的变动提醒，不判定机构意图或胜负。"""
        if not isfinite(提醒阈值) or 提醒阈值 <= 0:
            raise ValueError("提醒阈值必须为正有限数")
        return self.平赔变动值 <= -提醒阈值


@dataclass
class 赔率快照:
    """聚合根实体：带时间戳与赛事身份的心电图观测点"""
    比赛编号: str
    竞彩场次: str  # 例如: "周一002"
    对阵名称: str  # 例如: "赫塔费 vs 塞尔塔"
    联赛名称: str
    赔率: 赔率数值
    记录时间戳: int
    官方浮动标记: int  # -1 降水, 0 未变, 1 升水
    市场类型: str = "had"
    让球数: str = ""

    def 同一市场(self, 其他: "赔率快照") -> bool:
        return (self.比赛编号, self.市场类型, self.让球数) == (其他.比赛编号, 其他.市场类型, 其他.让球数)

    def 计算位移(self, 早期快照: "赔率快照") -> 赔率位移:
        """只比较同场、同市场、同让球线且时间递增的观测。"""
        if not self.同一市场(早期快照) or self.记录时间戳 <= 早期快照.记录时间戳:
            raise ValueError("快照市场不一致或时间未递增")
        变动 = self.赔率.平局 - 早期快照.赔率.平局
        小时差 = max(1.0 / 3600.0, (self.记录时间戳 - 早期快照.记录时间戳) / 3600.0)
        速率 = 变动 / 小时差

        if 变动 < 0:
            信号 = "平项赔率下降（原因待核验）"
        elif 变动 > 0:
            信号 = "平项赔率上升（原因待核验）"
        else:
            信号 = "中性平稳横盘"

        return 赔率位移(
            平赔变动值=变动,
            每小时变盘速率=速率,
            异动信号=信号
        )


def 校验让球明牌平局对冲资格(
    受让方场均客场失球: Optional[float],
    豪门休赛天数: Optional[float] = None,
    豪门预期进球xG: Optional[float] = None
) -> Tuple[Optional[bool], str]:
    """
    兼容旧名称；返回 None 表示未决，不等于不合格或推荐。
    这些指标缺少双方完整概率、样本量及价格，不能产生准入结论。
    """
    for value in (受让方场均客场失球, 豪门休赛天数, 豪门预期进球xG):
        if value is not None and (not isfinite(value) or value < 0):
            raise ValueError("场均失球、休赛天数和xG必须非负且有限")
    return None, (f"待评估：客场失球={受让方场均客场失球}，休赛天数={豪门休赛天数}，"
                  f"强方xG={豪门预期进球xG}；补齐双方攻防、样本及价格；缺少had不构成内幕证据")


def 校验攻防伤停平局资格(
    进攻核心缺阵: bool,
    后腰防线对抗率: Optional[float],
    主队场均失球: Optional[float] = None
) -> Tuple[Optional[bool], str]:
    """
    兼容旧名称；伤停影响需要结合位置、替代者及对手，不能由单一对抗率裁决。
    """
    if 后腰防线对抗率 is not None and (not isfinite(后腰防线对抗率) or not 0 <= 后腰防线对抗率 <= 1):
        raise ValueError("对抗率必须在0至1之间")
    if 主队场均失球 is not None and (not isfinite(主队场均失球) or 主队场均失球 < 0):
        raise ValueError("场均失球必须非负且有限")
    return None, (f"待评估：进攻核心缺阵={进攻核心缺阵}，对抗率={后腰防线对抗率}，"
                  f"场均失球={主队场均失球}；核验样本、替补与双方预期进球，不直接排除平局")


def 校验深盘冷平放行资格(
    强方胜赔: float,
    平局赔率: float,
    弱方场均失球: Optional[float] = None,
    强方休赛天数: Optional[float] = None
) -> Tuple[bool, str]:
    """
    红线 1 破除死板误杀断路器：
    强队胜赔 < 1.60 严禁机械一刀切否决！
    若弱方具备铁桶防守 (场均失球 <= 0.9)、或强方多赛体能透支 (休赛 <= 3 天)、或平赔高挂 (>= 3.50)，
    必须坚决放行并启动【冷平狙击/受让不败】复核！
    """
    if 强方胜赔 >= 1.60:
        return True, "合格：非深盘，正常纳入均势/博弈推演"
    # 排除防线极其脆弱的被打穿局
    if 弱方场均失球 is not None and 弱方场均失球 > 1.5:
        return False, f"排除：弱方防线千疮百孔 (失球={弱方场均失球}>1.5)，难以抵御强队碾压"
    # 深盘场景下的三大有效放行特征
    if 弱方场均失球 is not None and 弱方场均失球 <= 0.9:
        return True, f"放行：弱方防守坚韧 (失球={弱方场均失球}<=0.9)，严禁机械误杀，启动冷平复核"
    if 强方休赛天数 is not None and 强方休赛天数 <= 3.0:
        return True, f"放行：强方多赛双赛体能枯竭 (休赛={强方休赛天数}<=3天)，防爆冷绝平"
    if 3.40 <= 平局赔率 <= 4.60:
        return True, f"放行：平赔高挂={平局赔率}位于[3.40, 4.60]阻盘区间，符合高平阻盘通杀两头特征"
    return False, "排除：无铁桶/多赛/阻盘冷平特征"

