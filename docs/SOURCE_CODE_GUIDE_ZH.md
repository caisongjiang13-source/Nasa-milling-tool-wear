# 源代码、注释与整理版的对照说明

本次以你上传的 `Mill_phase_2_Fixed.ipynb` 为依据。之前的发布版保留了计算思路，但重新写成函数和脚本，原单元、变量名和注释没有完整展示。这一版把你的学习代码作为主要入口。

## 先看哪份文件

| 文件 | 内容 | 建议用途 |
| --- | --- | --- |
| [Mill_phase_2_Fixed.ipynb](../notebooks/Mill_phase_2_Fixed.ipynb) | 你上传文件的完整副本，代码、注释、markdown、元数据和已有输出都保留 | 查看原样内容 |
| [01_case1_exploration.ipynb](../notebooks/01_case1_exploration.ipynb) | 按原顺序保留全部单元，增加带标记的解释和必要修正 | 阅读、运行和继续学习 |
| [analysis.py](../src/analysis.py) | ChatGPT 协助重构的可选导出脚本，文件开头说明了来源 | 用命令快速导出表格和图片 |

阅读版直接运行你的特征计算代码，不再通过 `load_features()` 隐藏这些步骤。`number`、`VB_work`、`mask_cut`、`vib_spindle_cut_mean`、`a_vibs` 等变量保持可见。你注释掉的输入实验和检查语句也都保留。

**原样保留的范围：**可核验的是你上传的这个文件。它已有的 `restoration` 元数据记录了此前从粘贴的 Colab 内容恢复换行和缩进的过程；此次没有改动该元数据。没有恢复前的原始导出文件，就无法核对当时每个空格。你此后在 Colab 中做过、尚未上传的修改也不在这个快照里。

## 怎么判断哪些内容是新增的

- 你原来的代码、注释和 markdown 保持原顺序。
- 新解释单元以 **“整理说明 / Editorial note”** 开头。
- 修改过的代码有就近说明，并在单元元数据中记录 `source_cell_index` 和 `editorial_changes`。
- 原 notebook 结束后，新加的 AE 拟合、MAE、结果导出和发布图，都在 **“整理补充 / Publication additions”** 下。

准确对照见 [source_cell_map.json](source_cell_map.json)。其中的单元编号从零开始，`unchanged` 表示代码或文字内容与上传文件一致；`edited_with_note` 表示有记录的修改。保存输出重新计算，因此阅读版的执行编号、图片和输出不要求与原文件逐字节一致。

## 必要修改有哪些

| 原单元索引 | 修改 | 原因 |
| --- | --- | --- |
| `0` | 给原 Drive 挂载代码加 `IN_COLAB` 条件 | 本地运行可以跳过 Colab 专用操作 |
| `1, 2` | 数据路径改为 `DATA_PATH` | 方便修改自己的数据位置；保留重复检查单元 |
| `11, 14–19` | 波形横轴改标为未核实的假定时间坐标 | 保留 `t_s`、窗口和数据，避免把假定坐标说成已核实的秒数 |
| `20, 41` | 只调整标题 f-string 的外层引号 | 兼容较早的 Python 版本，不改变图的数据 |
| `36` | `print(a_vibs,b_vibs)` 改成 `print(a_AEs,b_AEs)` | 这个单元拟合振动标准差，原打印的是振动均值模型系数 |

原单元 `36` 的 `a_AEs`、`b_AEs` 名字仍保留，旁边说明它们实际代表振动标准差模型。原 markdown 中把标准差结果写成 “mean” 的文字也保留，随后加了更正说明。这样可以看到原来的思考和实际修正。

## 为什么 AE 拟合被标成补充代码

上传文件已有 AE 均值、标准差、相关性和特征表，但没有后来截图中的 AE 均值拟合与 MAE 代码。因此这部分是按后续结果补齐的代码，由 ChatGPT 协助准备，不能当作从原 notebook 原样复制的内容。

以后上传你最新的 Colab notebook，就可以把这部分换成你的实际实现，继续保留自己的注释。

## 图中的数字怎么改

在阅读版找到 **“Publication comparison and label positions”**，下面的 `label_offsets` 字典就是发布对比图的标签偏移。

```python
label_offsets = {
    'vib_mean': {8: (6, 11), 9: (-14, -14), 13: (-20, -8), 14: (-8, 14), 17: (7, -3)},
    'AE_mean': {},
}
```

这些数值只是为当前图选择的位置，不是分析结果。第一个偏移控制左右，第二个偏移控制上下；`textcoords='offset points'` 以排版点为单位。移开的标签加了细连接线，方便看清对应的点。参见 [Matplotlib 官方 annotate 文档](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html)。

修改后重新运行相应绘图单元，再下载 `figures/feature_relationships.png` 上传到 GitHub。网页显示的是上传的图片文件，改代码后仍需生成和更新图片。

## 核验依据

- [source_cell_map.json](source_cell_map.json)：原文件 SHA-256、单元顺序和修改记录。
- [VALIDATION.md](VALIDATION.md)：原文件完整性、注释保留、数值与执行检查。
- [case1_features.csv](../results/case1_features.csv)、[baseline_metrics.csv](../results/baseline_metrics.csv)：这次直接沿用原计算生成的结果。

感悟部分继续留空，由你自己填写。
