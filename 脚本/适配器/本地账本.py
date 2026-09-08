"""
DDD 输出适配器 - SQLite 赔率心电图连续账本
负责在结构化本地数据目录中存储和检索时序快照
"""
import os
import sqlite3
from typing import List, Optional

from 领域.模型 import 赔率数值, 赔率快照
from 领域.契约 import 赔率账本契约


class 本地账本仓储(赔率账本契约):
    """实现赔率账本契约，基于轻量高效的标准库 SQLite"""

    def __init__(self, 数据库路径: str):
        self.数据库路径 = 数据库路径
        os.makedirs(os.path.dirname(os.path.abspath(数据库路径)), exist_ok=True)
        self._初始化表结构()

    def _初始化表结构(self) -> None:
        with sqlite3.connect(self.数据库路径) as 连接:
            连接.execute("""
                CREATE TABLE IF NOT EXISTS 赔率时序流水 (
                    序号 INTEGER PRIMARY KEY AUTOINCREMENT,
                    比赛编号 TEXT NOT NULL,
                    竞彩场次 TEXT NOT NULL,
                    对阵名称 TEXT NOT NULL,
                    联赛名称 TEXT NOT NULL,
                    主胜赔率 REAL NOT NULL,
                    平局赔率 REAL NOT NULL,
                    客胜赔率 REAL NOT NULL,
                    记录时间戳 INTEGER NOT NULL,
                    官方浮动标记 INTEGER NOT NULL
                )
            """)
            连接.execute("""
                CREATE INDEX IF NOT EXISTS 索引_场次时间 
                ON 赔率时序流水(竞彩场次, 记录时间戳)
            """)
            连接.commit()

    def 批量保存快照(self, 快照列表: List[赔率快照]) -> None:
        if not 快照列表:
            return
        记录列表 = [
            (
                快照.比赛编号,
                快照.竞彩场次,
                快照.对阵名称,
                快照.联赛名称,
                快照.赔率.主胜,
                快照.赔率.平局,
                快照.赔率.客胜,
                快照.记录时间戳,
                快照.官方浮动标记
            )
            for 快照 in 快照列表
        ]
        with sqlite3.connect(self.数据库路径) as 连接:
            连接.executemany("""
                INSERT INTO 赔率时序流水 (
                    比赛编号, 竞彩场次, 对阵名称, 联赛名称,
                    主胜赔率, 平局赔率, 客胜赔率,
                    记录时间戳, 官方浮动标记
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 记录列表)
            连接.commit()

    def 查询比赛连续轨迹(self, 竞彩场次: str) -> List[赔率快照]:
        with sqlite3.connect(self.数据库路径) as 连接:
            游标 = 连接.cursor()
            游标.execute("""
                SELECT 比赛编号, 竞彩场次, 对阵名称, 联赛名称,
                       主胜赔率, 平局赔率, 客胜赔率,
                       记录时间戳, 官方浮动标记
                FROM 赔率时序流水
                WHERE 竞彩场次 = ?
                ORDER BY 记录时间戳 ASC
            """, (竞彩场次,))
            记录 = 游标.fetchall()

        return [
            赔率快照(
                比赛编号=行[0],
                竞彩场次=行[1],
                对阵名称=行[2],
                联赛名称=行[3],
                赔率=赔率数值(主胜=行[4], 平局=行[5], 客胜=行[6]),
                记录时间戳=行[7],
                官方浮动标记=行[8]
            )
            for 行 in 记录
        ]

    def 获取最新快照(self, 竞彩场次: str) -> Optional[赔率快照]:
        with sqlite3.connect(self.数据库路径) as 连接:
            游标 = 连接.cursor()
            游标.execute("""
                SELECT 比赛编号, 竞彩场次, 对阵名称, 联赛名称,
                       主胜赔率, 平局赔率, 客胜赔率,
                       记录时间戳, 官方浮动标记
                FROM 赔率时序流水
                WHERE 竞彩场次 = ?
                ORDER BY 记录时间戳 DESC
                LIMIT 1
            """, (竞彩场次,))
            行 = 游标.fetchone()

        if not 行:
            return None

        return 赔率快照(
            比赛编号=行[0],
            竞彩场次=行[1],
            对阵名称=行[2],
            联赛名称=行[3],
            赔率=赔率数值(主胜=行[4], 平局=行[5], 客胜=行[6]),
            记录时间戳=行[7],
            官方浮动标记=行[8]
        )
