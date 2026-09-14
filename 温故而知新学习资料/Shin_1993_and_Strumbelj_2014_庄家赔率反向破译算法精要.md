# Shin与比例归一化：方法说明及适用边界

这是项目编写的方法笔记，不是论文原文。现行[分析规程](../AGENTS.md)要求区分市场概率与独立模型；[规则审计](../分析复盘记录/README.md#rule-audit)记录旧笔记的公式与解释错误。

令十进制赔率为 $o_i$、倒数为 $q_i=1/o_i$、$B=\sum_i q_i$。
比例归一化为 $p_i=q_i/B$。它是可比较的基准方法，不是“幼稚错误”；本项目`赔率数值.去水公平概率()`实际采用此法，没有实现Shin。

Shin常用逆变换为：

$$p_i(z)=\frac{\sqrt{z^2+4(1-z)q_i^2/B}-z}{2(1-z)}.$$

选择使 $\sum_i p_i(z)=1$ 的模型参数 $z$，并验证求解收敛、概率合法及输入适用性。旧笔记漏掉了 $q_i^2/B$，其固定搜索区间与末尾归一化不能弥补该错误，原示例数值撤回。
公式已对照[实现作者维护的源码](https://github.com/mberk/shin/blob/master/python/shin/__init__.py)核验；没有在本项目新增另一份求解器。

$z$是给定建模假设下推得的潜在参数，不是独立观测的内幕交易比例，更不能直接判断假球、战术犯规或庄家单场意图。求得的概率同样需要样本外验证。
比例、Shin和幂方法应在同样的场次、时点与指标上比较。幂方法的指数通常也要数值求解；不能笼统声称它无需迭代。

[跨市场比较研究](https://link.springer.com/article/10.1007/s10479-022-04722-3)发现方法表现随联赛不同：其英超样本下Shin估计表现较好，西甲中两种方法仍存在偏差。不能推导出“Shin永远最佳”或“能精确反推真实概率”。

原始方法来源：Hyun Song Shin (1993), *Measuring the Incidence of Insider Trading in a Market for State-Contingent Claims*；Erik Štrumbelj (2014), *On determining probability forecasts from betting odds*。
其他材料见[文献导读](README.md#classic-papers)与[智慧复盘论文索引](README.md#review-papers)。
