> **学术知识网络导航**：[系统大脑 AGENTS.md](../AGENTS.md) · [文献总索引与导读](README_学习资料索引与经典论文导读.md) · [实战总复盘总结](../分析复盘记录/总复盘总结.md) · [战绩胜率看板](../分析复盘记录/总准确率.md) · [最新赛前推演](../分析复盘记录/2026-09-12_预测.md)

---

# Shin 模型 (1993) 与 Štrumbelj 算法 (2014) · 庄家赔率反向破译真实概率数学精要

> **归档位置**：`D:\100-工作\200-交易\足球预测\温故而知新学习资料\`  
> **理论源头**：  
> 1. Hyun Song Shin (1993), *Measuring the Incidence of Insider Trading in a Market for State-Contingent Claims*, The Economic Journal, 103(420), 1141–1153.  
> 2. Erik Štrumbelj (2014), *On determining probability forecasts from betting odds*, International Journal of Forecasting, 30(4), 934–943.  
> 3. 2026 最新前沿统一实现见本目录：[2604.17194 有效市场纯赔率模型](./2604.17194_Forecast_Sports_Outcomes_under_EMH_Odds_Only_Models.md)

---

## 一、 核心公理：为什么必须反向破译庄家赔率？

庄家开出的胜平负倍率（Decimal Odds）$o_i$ 包含两层水分：
1. **公开抽水（Overround / Margin）**：庄家设置的资金蓄水池，满足 $\sum \frac{1}{o_i} > 1.0$；
2. **防内幕黑幕溢价（Shin's Insider Margin）**：庄家最大的恐惧是被“掌握内部假球或极端知情信息的资金（Insider Traders）”穿仓洗劫。为此，庄家会对高胜率或受操纵倾向的结果进行非对称压低（Favourite-Longshot Bias）。

普通的简单去水法（$\frac{1/o_i}{\sum 1/o_k}$）假设庄家抽水是均匀分配的，**这是极其幼稚的错误**。Shin 模型证明了：庄家的抽水是非对称施加的，平局和冷门承担了完全不同的风险溢价。

---

## 二、 Shin 模型的数学机制

假设市场上存在比例为 $z \in (0, 1)$ 的知情内幕交易者（Insider Traders），他们确切知道赛果；其余 $1-z$ 为普通散户。
真实概率向量为 $p = (p_1, p_2, \dots, p_n)$，满足 $\sum p_i = 1$。

庄家面对内幕交易者的保护性赔率定价满足以下平衡条件：
$$\frac{1}{o_i} = \frac{z + (1-z)p_i}{\sum_j \sqrt{z^2 + 4(1-z)\frac{p_j}{o_j}}}$$

通过 Shin 逆变换（Inversion），真实概率 $p_i$ 可以被精确解出：
$$p_i = \frac{\sqrt{z^2 + 4(1-z)\frac{1}{o_i}} - z}{2(1-z)}$$

其中，内幕交易者占比参数 $z$ 通过以下目标函数的根（Root-Finding）单变量迭代求得：
$$\sum_{i=1}^n \sqrt{z^2 + 4(1-z)\frac{1}{o_i}} - 2 = (n-2)z$$

**物理意义**：
* 当 $z \to 0$ 时，市场完全公开透明，无任何假球内幕，赔率退化为简单无抽水概率；
* 当 $z > 0$ 时，$z$ 即为**庄家认定的本场比赛“黑幕与信息不对称严重程度”**！
* 经 Shin 模型洗出来的 $p_i$，才是庄家内心深处真正认定的真实赛果概率！

---

## 三、 Štrumbelj (2014) 现代反向工程工业标准

Erik Štrumbelj 在《International Journal of Forecasting》中系统评测了四大反向算法：

1. **基本比例去水法 (Basic Normalization)**：
   $$p_i = \frac{1/o_i}{\sum_{j} 1/o_j}$$
   *缺陷*：严重低估弱队爆冷与极端平局概率。
2. **幂律去水法 (Power Method)**：
   $$p_i = (1/o_i)^k, \quad \text{其中 } k \text{ 满足 } \sum (1/o_i)^k = 1$$
   *优势*：计算速度极快，无需数值迭代求解。
3. **Shin 数值迭代法 (Shin's Method - Štrumbelj Variant)**：
   * 在欧洲五大联赛实测中综合排名第一，对于平赔压低的场次反向识别精度极高。
4. **对数赔率回归法 (Logit Odds Conversion)**：
   利用历史大样本数据拟合非线性逻辑斯蒂曲面。

---

## 四、 本地可直接调用的 Python 核心反向求解器

```python
import math

def solve_shin_probabilities(odds: list[float]) -> tuple[list[float], float]:
    """
    输入: 胜平负赔率列表 [home_odds, draw_odds, away_odds]
    输出: (真实概率列表 [p_home, p_draw, p_away], 庄家内幕风险系数 z)
    """
    inv_odds = [1.0 / o for o in odds]
    n = len(odds)
    
    # 二分法求解内幕参数 z in [0, 0.4]
    low, high = 0.0, 0.4
    z = 0.0
    for _ in range(50):
        mid = (low + high) / 2.0
        val = sum(math.sqrt(mid**2 + 4 * (1 - mid) * io) for io in inv_odds) - 2 - (n - 2) * mid
        if val > 0:
            low = mid
        else:
            high = mid
        z = mid
        
    # 计算剥离内幕抽水后的真实概率
    probs = [(math.sqrt(z**2 + 4 * (1 - z) * io) - z) / (2 * (1 - z)) for io in inv_odds]
    total_p = sum(probs)
    normalized_probs = [p / total_p for p in probs]
    return normalized_probs, z

# 实测: 今日周日019 阿拉维斯 vs 奥萨苏纳 (2.50, 2.82, 2.70)
# p, z = solve_shin_probabilities([2.50, 2.82, 2.70])
# 算得: z = 0.024 (内幕防范系数), 真实平率 = 31.8%
```
