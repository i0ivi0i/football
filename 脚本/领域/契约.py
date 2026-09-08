"""
DDD 领域端口契约 - 抽象基类定义输入与输出边界
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from 领域.模型 import 赔率快照


class 赔率提供者契约(ABC):
    """输入/输出端口：从外部获取最新的实时赔率快照"""

    @abstractmethod
    def 抓取当前快照列表(self) -> List[赔率快照]:
        pass


class 赔率账本契约(ABC):
    """输出端口：心电图轨迹的数据持久化与历史回溯"""

    @abstractmethod
    def 批量保存快照(self, 快照列表: List[赔率快照]) -> None:
        pass

    @abstractmethod
    def 查询比赛连续轨迹(self, 竞彩场次: str) -> List[赔率快照]:
        pass

    @abstractmethod
    def 获取最新快照(self, 竞彩场次: str) -> Optional[赔率快照]:
        pass
