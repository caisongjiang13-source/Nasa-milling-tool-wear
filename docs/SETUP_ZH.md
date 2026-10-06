# 安装、运行和更新 GitHub

这次以你的学习 notebook 为主要内容。README 首页直接链接原样版和阅读版。原样版完整保留上传文件，阅读版保留单元顺序、变量名和注释，并在新增说明和修正处加标记。

## 先打开什么

| 文件 | 用途 |
| --- | --- |
| `notebooks/Mill_phase_2_Fixed.ipynb` | 看你上传的代码、注释和已有输出，文件内容未改 |
| `notebooks/01_case1_exploration.ipynb` | 读解释、运行原计算、继续修改 |
| `docs/SOURCE_CODE_GUIDE_ZH.md` | 查哪些地方原样保留、哪些地方修正或补充 |
| `src/analysis.py` | 可选的整理脚本，用命令导出结果 |
| `figures/`、`results/` | 已生成的真实图片和结果表 |
| `docs/LEARNING_LOG.md` | 继续记录自己的思考，感悟仍留空 |

数据 `mill.mat` 不在发布包里。原样版保留原来的 Drive 路径；阅读版在第一个新增代码单元设置 `DATA_PATH`，可以改成你实际的数据位置。

## 更新你现在的 GitHub 仓库

1. 下载并解压新版 `NASA_Milling_GitHub_Package.zip`。
2. 打开现有仓库：[Nasa-milling-tool-wear](https://github.com/caisongjiang13-source/Nasa-milling-tool-wear)。
3. 在仓库根目录选 `Add file → Upload files`。
4. 拖入解压后 `nasa-milling-tool-wear` **里面的文件和子文件夹**。不要拖外层文件夹，否则 README 会被套在里面；也不要把 ZIP 直接当作代码上传。
5. 确认 `README.md` 在根目录，`notebooks` 中有原样版和阅读版；同名路径的文件将更新为新版。上传不会删除其他文件；如果你之后另加过自己的内容，先核对相应同名文件。
6. 提交说明可用 `Preserve original learning notebook and clarify assisted edits`，点 `Commit changes`。
7. 回仓库首页刷新，打开 README 的原 notebook 链接，确认能看到自己的变量名、循环和注释；再检查首页图片。

发布包不包含原始数据、虚拟环境或缓存。浏览器上传需要自行选择文件；GitHub 网页上传不会自动应用本地忽略规则。上传流程参考 [GitHub 官方文档](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。

GitHub 会把 notebook 渲染成可读页面，别人可以直接看到代码和已保存输出；运行仍需要 Colab 或本地 Python 环境。参考 [GitHub notebook 文档](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#working-with-jupyter-notebook-files-on-github)。

## Colab：直接运行阅读版

1. 打开 [Google Colab](https://colab.research.google.com/)，在打开笔记本窗口选择 `Upload`，上传 `notebooks/01_case1_exploration.ipynb`。
2. 按顺序运行。第一个新增代码单元设置数据路径；随后原 Drive 单元会连接你的 Drive。
3. 选择存有 `mill.mat` 的账号，按提示完成授权。
4. 默认读取你之前使用的 `/content/drive/MyDrive/mill.mat`。如果文件换了位置，在设置单元修改 `DATA_PATH`。
5. 继续依次运行下面的原始分析单元，直到新增的发布图和结果导出部分。

阅读版的核心计算已经写在各个单元里，因此可以单独运行这个 notebook。若没有解压整个项目，输出会写到当前目录下的 `results` 和 `figures`。若当前目录或 `/content/milling-project` 已有完整项目，输出会写到该项目目录。

Colab 如提示缺少库，可添加临时代码单元运行：

```python
%pip install numpy scipy pandas matplotlib
```

Colab 运行环境结束后，其临时文件可能丢失；完成后下载 notebook，或保存到自己的 Drive。Drive 访问和文件下载参照 [Colab 官方数据示例](https://colab.research.google.com/notebooks/io.ipynb)。

## 如果继续使用现在的 Colab 项目

先完成上面的 GitHub 上传，然后在当前 Colab 中新建代码单元并运行：

```python
%cd /content/milling-project
!git pull
!python src/analysis.py --data "/content/drive/MyDrive/mill.mat"
```

这是运行可选导出脚本。阅读自己的学习过程时，打开 `notebooks` 中的阅读版。该脚本的功能和来源见文件开头。

显示并下载生成的图片：

```python
from IPython.display import Image, display
from google.colab import files

display(Image(filename="/content/milling-project/figures/feature_relationships.png"))
files.download("/content/milling-project/figures/feature_relationships.png")
```

只改 GitHub 代码不会自动生成图片。运行后，去 GitHub 的 `figures` 文件夹上传新的同名 PNG，再保存提交。下载文件若被电脑加上 `(1)`，先改回 `feature_relationships.png`。

## Windows：安装和运行

1. 从 [Python 官网](https://www.python.org/downloads/) 安装 Python。项目数值计算在 Python 3.12 环境验证，具体版本见 [VALIDATION.md](VALIDATION.md)。
2. 用 VS Code 打开解压后的 `nasa-milling-tool-wear` 文件夹，再打开终端。终端所在目录应能看到 `requirements.txt`。
3. 依次运行：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

4. 将自己的 `mill.mat` 复制到 `data` 文件夹。也可从 [NASA Milling 数据页面](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) 下载后解压。
5. 打开 notebook：

```powershell
.\.venv\Scripts\python.exe -m notebook
```

浏览器打开后，进入 `notebooks`，打开 `01_case1_exploration.ipynb`，按顺序运行。原样文件保留 Colab 代码；本地运行建议使用阅读版。

如果只想重新导出表格和图片，运行可选脚本：

```powershell
.\.venv\Scripts\python.exe src\analysis.py
```

安装命令参考 [Python 环境指南](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) 和 [Jupyter 官方安装文档](https://jupyter.org/install)。本次核验是在 Python 进程中执行计算；没有实测你的 Windows 或 Colab 环境。

## 改图中的数字

在阅读版找到 `label_offsets`，修改想调整的 run 对应偏移，再运行该绘图单元。具体示例和修改来源在 [源代码对照说明](SOURCE_CODE_GUIDE_ZH.md)。单个 `xytext` 偏移控制文字位置，不改变数据点或回归结果。

## LinkedIn 与感悟

新版文案说明仓库包含学习 notebook，并标明整理过程有 ChatGPT 协助。GitHub 地址已经填好；先完成仓库更新，再发布。

- 自己填写 `LinkedIn_Post_EN.md` 的感悟位置，不要把占位符一起发出去。
- 可附上按文件名排序的图片，或使用同内容的 PDF。
- 下一步仍是计划；没有完成独立验证和组合模型。

感悟可选写：你对信号与刀具磨损的关系原本怎么想；哪处异常或残差让你重新思考；下一步最想验证什么。具体内容由你自己决定。
