# 安装、运行和发布指南

这里有两件不同的事：把项目上传到 GitHub，让别人查看；以及在自己的电脑上安装 Python 环境，让代码运行。上传本身不需要安装 Git 或 Python。

## 先认识发布包

解压 `NASA_Milling_GitHub_Package.zip` 后，会得到 `nasa-milling-tool-wear` 文件夹。

- `README.md`：别人打开 GitHub 仓库首先看到的英文介绍。
- `notebooks/01_case1_exploration.ipynb`：带解释、代码和保存输出的 notebook。
- `src/analysis.py`：运行后重建结果表和图片。
- `requirements.txt`：所需 Python 包。
- `results/`、`figures/`：真实结果与图，可直接查看。
- `docs/LEARNING_LOG.md`：之后记录思考和修改；感悟留空。

数据不在压缩包里。README、日志和 LinkedIn 文案的感悟位置都由你自己补充。GitHub 软件许可证尚未选择；这是草稿中的待定项。

## 上传到 GitHub：可以先完成这一步

1. 登录 [GitHub](https://github.com/)，打开 [新建仓库页面](https://github.com/new)。
2. 仓库名建议填写 `nasa-milling-tool-wear`。描述可直接填写：

   `Exploring spindle vibration and acoustic emission features for tool-wear estimation using the NASA Milling dataset.`

3. 选择 Public。这个发布包已经有 README 和忽略规则，不需要额外生成。许可证可以之后再选。
4. 创建仓库后，选择上传文件的入口；通常是 `Add file → Upload files`，空仓库页面也可能直接显示上传链接。
5. 将解压后 `nasa-milling-tool-wear` 文件夹里面的文件和子文件夹拖进去。让 `README.md` 直接位于仓库根目录，避免多套一层文件夹。不要直接上传 ZIP 代替代码。
6. 确认 `src/`、`notebooks/`、`figures/`、`results/`、`docs/`、`data/README.md` 和 `requirements.txt` 都在。若文件选择器没显示忽略规则文件，可以通过 GitHub 的新建文件功能添加包里的 `.gitignore` 内容。
7. 提交说明可填写 `Add exploratory tool-wear analysis and reproducible results`，然后保存提交。根据界面可能显示 `Commit changes` 或 `Propose changes`。
8. 打开仓库首页，检查 README 图片和 notebook 是否可读。将仓库网址填入 LinkedIn 文案。

**浏览器上传不会自动遵守忽略规则。** 当前压缩包没有原始数据和虚拟环境；以后更新时，手动确认没有把 `mill.mat` 或 `.venv` 拖进去。

以上流程参照 [GitHub 创建仓库文档](https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github) 和 [上传文件文档](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。GitHub README 没有统一强制模板，本包参考了 [官方介绍建议](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) 与同类项目结构。

## Windows：安装和运行

这些命令在 Windows 的 VS Code 终端或 PowerShell 中运行。

1. 从 [Python 官网](https://www.python.org/downloads/) 安装 Python。安装后运行 `py --version`，确认命令能找到 Python。本项目的数值计算在 Python 3.12 环境下验证，具体版本见 `docs/VALIDATION.md`。
2. 用 VS Code 的“打开文件夹”选择解压后的 `nasa-milling-tool-wear`，然后打开终端。终端应位于这个文件夹里，能看到 `requirements.txt`。
3. 逐行执行：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

第一行建立本项目独立的 Python 环境；第二行安装所需库。这里直接调用环境中的 Python，无需修改 PowerShell 的脚本执行策略。

4. 从 [NASA 数据页面](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/) 下载 Milling 数据，解压后把 `mill.mat` 放入项目的 `data` 文件夹。如果你已保存自己的 `mill.mat`，可以直接复制过去。
5. 运行：

```powershell
.\.venv\Scripts\python.exe src\analysis.py
```

运行成功会打印模型结果，更新 `results/` 的 CSV 和 `figures/` 的 PNG。这里只是复现现有分析，没有独立测试集。

6. 如果希望像 Colab 一样按单元学习，运行：

```powershell
.\.venv\Scripts\python.exe -m notebook
```

浏览器打开后，进入 `notebooks`，打开 `01_case1_exploration.ipynb`，按顺序运行。你也可以在 VS Code 中安装 Python 和 Jupyter 扩展，打开 notebook 并选择 `.venv` 内的解释器。

命令参照 [Python 环境安装指南](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) 和 [Jupyter 安装文档](https://jupyter.org/install)。

## Colab：继续沿用你熟悉的方式

本版代码会读取 `src/analysis.py`，因此要上传并解压整个 GitHub 发布包，不能只上传 notebook。

1. 在 Colab 打开包里的 `notebooks/01_case1_exploration.ipynb`。
2. 用左侧文件面板上传 `NASA_Milling_GitHub_Package.zip`。
3. 在 notebook 最前面临时添加一个代码单元：

```python
import zipfile
with zipfile.ZipFile('/content/NASA_Milling_GitHub_Package.zip') as archive:
    archive.extractall('/content')
```

4. 文件面板刷新后，把 `mill.mat` 上传到 `/content/nasa-milling-tool-wear/data/`。也可以从你已挂载的 Google Drive 复制：

```python
from google.colab import drive
import shutil
drive.mount('/content/drive')
shutil.copy('/content/drive/MyDrive/mill.mat',
            '/content/nasa-milling-tool-wear/data/mill.mat')
```

5. 从发布 notebook 的第一个原有单元开始按顺序运行。如果提示缺少库，可在临时单元运行：

```python
%pip install -r /content/nasa-milling-tool-wear/requirements.txt
```

Colab 的 `/content` 文件会随运行环境结束而丢失；有新进度时下载 notebook 或保存到你自己的 Drive。上述路径必须与实际文件名一致。

## 常见情况

| 提示 / 情况 | 检查与处理 |
| --- | --- |
| `py` 不存在 | 检查 Python 是否安装；若 `python --version` 正常，可用 `python` 替代 `py` |
| 找不到 `requirements.txt` | 终端没有位于项目根目录；重新打开正确文件夹 |
| 找不到 `mill.mat` | 将文件放到 `data/mill.mat`，或用 `--data` 指定实际路径 |
| 找不到 `src/analysis.py` | 没有解压整个项目，或 notebook 在不相关文件夹里运行 |
| GitHub 首页只显示一个文件夹 | README 没有放在根目录；把内层文件上传到仓库根目录 |
| 图里没有秒或毫米 | 尚未核实物理时间与单位，先保留样本位置和数据单位，避免误标 |

## LinkedIn 发布

- 修改 `LinkedIn_Post_EN.md` 的感悟占位和 GitHub 网址。
- 按文件名顺序附上 `LinkedIn_01.png`、`LinkedIn_02.png`、`LinkedIn_03.png`。也提供了同内容的 `LinkedIn_Project_Carousel.pdf`，可以在支持文档发布的入口使用。
- 没有填感悟之前，不要把占位文字一起发布。不想写感悟时，直接删除那一行即可。
- 文案中的下一步仍是计划；不要写成已经完成多特征预测、独立验证或 AI 模型。

## 感悟可以从这些问题里选

这里不替你写答案。你可以先用中文写。

- 开始前你以为信号与磨损会是什么关系？实际哪里让你意外？
- 哪张残差图改变了你对“相关性强就能预测准”的理解？
- 调试中遇到什么具体问题，你最后怎么理解它？
- 下一步你最想验证什么，为什么？

不需要每题都答。挑真正符合你的经历的内容，我们再一起改成自然英文。
