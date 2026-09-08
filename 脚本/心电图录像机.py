"""
足球倍率心电图连续录像机 - 组装根 (Composition Root)
纯正 10/10 DDD 洋葱整洁架构，信达雅全中文命名
"""
import argparse
import os
import sys
import time
from datetime import datetime

当前目录 = os.path.dirname(os.path.abspath(__file__))
if 当前目录 not in sys.path:
    sys.path.insert(0, 当前目录)

from 领域.契约 import 赔率提供者契约, 赔率账本契约
from 适配器.体彩接口 import 体彩官方适配器
from 适配器.本地账本 import 本地账本仓储
from 应用.用例 import 探测并记录心电图用例, 回溯连续轨迹用例

数据目录 = os.path.join(当前目录, "数据")
默认账本路径 = os.path.join(数据目录, "赔率心电图.db")


def 组装架构(账本路径: str = 默认账本路径):
    账本: 赔率账本契约 = 本地账本仓储(数据库路径=账本路径)
    提供者: 赔率提供者契约 = 体彩官方适配器()
    记录用例 = 探测并记录心电图用例(提供者=提供者, 账本=账本)
    分析用例 = 回溯连续轨迹用例(账本=账本)
    return 记录用例, 分析用例, 账本


def 执行单次探测(记录用例: 探测并记录心电图用例):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 💓 正在探测体彩官方盘口并记录心电图快照...")
    结果 = 记录用例.执行()
    print(f"✅ 成功记录 {结果.入库数量} 场比赛快照至结构化账本！")
    if 结果.异常异动警报:
        print("\n🚨 【捕获显著倍率异常异动警报】:")
        for 警报 in 结果.异常异动警报:
            print(f"  ⚡ {警报.异动信号}: 平赔变动 {警报.平赔变动值:+.2f} | 变盘速度 {警报.每小时变盘速率:+.2f}/小时")
    else:
        print("⚖️ 盘面相对平稳，未检测到突发剧烈变盘。")


def 展示比赛轨迹(分析用例: 回溯连续轨迹用例, 竞彩场次: str):
    结果 = 分析用例.分析单场(竞彩场次)
    if 结果.采样次数 == 0:
        print(f"⚠️ 账本中暂无比赛 [{竞彩场次}] 的历史轨迹。")
        return

    首盘 = 结果.历史快照列表[0]
    print(f"\n📈 【{首盘.竞彩场次} {首盘.对阵名称} ({首盘.联赛名称}) 赔率连续心电图】")
    print(f"  ⏱️ 采样次数: {结果.采样次数} 次 | 累计平赔位移: {结果.累计平赔位移:+.2f} | 态势定性: {结果.趋势定性}")
    print("  -------------------------------------------------------------")
    for 序号, 快照 in enumerate(结果.历史快照列表, 1):
        时间字串 = datetime.fromtimestamp(快照.记录时间戳).strftime('%H:%M:%S')
        主率, 平率, 客率 = 快照.赔率.去水公平概率()
        标记符号 = "🔻" if 快照.官方浮动标记 < 0 else ("🔺" if 快照.官方浮动标记 > 0 else "➖")
        print(f"  #{序号} [{时间字串}] 胜:{快照.赔率.主胜:4.2f} 平:{快照.赔率.平局:4.2f} 负:{快照.赔率.客胜:4.2f} | 公平平率:{平率*100:5.2f}% | 变动:{标记符号}")


def main():
    解析器 = argparse.ArgumentParser(description="足球倍率心电图连续录像机 (10/10 纯真DDD洋葱整洁架构)")
    解析器.add_argument("--单次探测", "--tick", action="store_true", help="单次抓取并记录")
    解析器.add_argument("--轨迹回溯", "--trajectory", type=str, help="查看某场比赛历史轨迹 (如: 周一002)")
    解析器.add_argument("--守护循环", "--loop", type=int, help="持续后台循环采样，指定间隔秒数 (如: 1800)")
    解析器.add_argument("--账本路径", "--db", type=str, default=默认账本路径, help="指定 SQLite 数据库路径")

    参数 = 解析器.parse_args()
    记录用例, 分析用例, _ = 组装架构(参数.账本路径)

    if 参数.轨迹回溯:
        展示比赛轨迹(分析用例, 参数.轨迹回溯)
    elif 参数.守护循环:
        间隔 = max(60, 参数.守护循环)
        print(f"🚀 启动心电图持续监听守护进程，采样间隔: {间隔} 秒...")
        try:
            while True:
                执行单次探测(记录用例)
                time.sleep(间隔)
        except KeyboardInterrupt:
            print("\n🛑 录像进程已安全停止。")
    else:
        执行单次探测(记录用例)


if __name__ == "__main__":
    main()
