# 足球概率分析与智慧复盘

本项目用可核查数据、市场参照与独立模型推演足球胜平负；践行全盘单一最佳价值模式（ADR-0001），以纯数学 +EV（ADR-0002）为唯一选拔基准，允许全日空仓。

## 使用入口

- [AGENTS分析规程](AGENTS.md)：证据边界、技能分工、八层分析与七类条件复核。
- [文档中枢 (docs)](docs/README.md)：推演前必读、必用、必执行的核心方法论中枢。
- [架构决策 ADR (0001-0016)](docs/adr/README.md)：核心系统架构决策与防幻觉物理门禁。
- [量化术语表](docs/glossary.md)：量化模型、交易策略与呈现术语定义。
- [复盘契约](分析复盘记录/README.md)：赛前记录、赛后解耦统计与习惯塑形流程。
- [经验与习惯塑形](分析复盘记录/总复盘总结.md)、[计数看板](分析复盘记录/总准确率.md)、[本次审计](分析复盘记录/README.md#rule-audit)。
- [论文库](温故而知新学习资料/README.md#classic-papers)、[智慧复盘论文](温故而知新学习资料/README.md#review-papers)。

## 量化架构与技能分工

- **双引擎融合做实（ADR-0014）**：
  - `football-match-analysis`：主责独立攻防泊松矩阵计算、Elo实力评分与纯数学 +EV 极值排序；
  - `football-betting-analysis`：主责主流做市商（体彩+Pinnacle+Bet365）真实赔率采样、Shin算法去水与 8 层博弈推演。
- **微观伤停泊松衰减（ADR-0004 / 0015）**：
  - 推演前强制调取真实伤停大名单，依据位置权重计算攻防参数衰减（$\Delta\alpha, \Delta\beta$），动态重构泊松分布与 +EV；
  - 缺失数据强制标注 `[N/A·缺失未测]` 水印并一票降级，彻底杜绝虚构方差与主观脑补。
- **做市商时序追踪与意图破译（ADR-0012 / 0013）**：
  - 比对初盘与即盘位移差（$|\Delta Odds| \ge 0.15$ 或 $|\Delta Water| \ge 8\%$ 自适应重估），捕捉 RLM 与做市商收割陷阱。
- **交付呈现（ADR-0005 / 0009）**：
  - 聊天窗口直出极简秒看卡片流，终审操作指令清晰（胜/平/负/观望空仓），刚性附带真实实测存活的 Polymarket 链接。

## 最小工作流程

赛前先通过系统物理时钟探测（datetime.now()）对齐真实日期，物理核对体彩官方实际在售清单，抓取双方首发伤停并执行泊松衰减与 +EV 排序。
赛后先遮盖赛果进行 Aiyer (2023) 学术解耦复盘，审查赛前逻辑与期望值，将教训沉淀入芯片，最后执行 `graphify update .` 同步知识图谱。

## 常用命令（PowerShell）

```powershell
# 知识图谱检索与自进化更新
graphify query '条件复盘 习惯塑形'
graphify update .

# 足球微观数据抓取（通过 sports-skills CLI）
sports-skills football get_missing_players --help
sports-skills football get_fixtures_by_date --date 2026-09-22
```

图谱更新使用官方工具；文档变更保持语义自洽，严格杜绝在仓库内创建任何私有 `.py` 代码文件。
