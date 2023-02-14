# python project using

## 虚拟环境配置

```python
virtualenv *_env
cd Scripts
./activate
```

## 虚拟环境进入

```py
1) conda activate python37
2) cd errbot_env/Scripts
3) ./activate
```

## 1. 项目工程类

### 1.1 errbot 聊天机器人

[项目地址](./errbot/)

#### 配置

```python
1. 环境
python37->errbot_env
2. 初始化
errbot --init
3. 进入
errbot
```

#### 使用

未完待续...

### 1.2 pylama 代码审计工具

[项目地址](./pylama_env/README.md)

#### 配置

```python
1. 环境
python37->pylame_env
2. 安装
pip install pylama[all]
```

#### 使用

pylama + 文件或文件夹

### 1.3 fsociety 模块化渗透测试框架

[项目地址](./fsociety_env/README.md)

### 配置

```python
1. 进入环境
python37->fsociety_env
2. 安装
需要在linux环境下
pip install fsociety
```

### 1.4 代码跟踪和分析工具

1. Hunter用于代码跟踪，不是用于测量覆盖率，而是用于调试，日志记录，检查和其他
   [Hunter项目网址](https://github.com/ionelmc/python-hunter)
2. Py-spy是Python程序的采样分析器
   [Py-spy项目网址](https://github.com/benfred/py-spy)

### 1.5 psutil --进程监控和系统利用率管理工具

[项目地址](./psutil_env/README.md)

### 1.6 barcode --条形码生成工具

[项目地址](./barcode_env/README.md)

### 1.7 qrcode --二维码生成器工具

[项目地址](./qrcode_env/README.md)

### 1.8 Youtube-dl --基于Python的下载视频的工具

允许从 YouTube、Dailymotion、Google Video、Photobucket、Facebook、Yahoo、Metacafe、Depositfiles、Bilibili 和类似网站下载视频
[项目地址](./Youtube_env/README.md)

#### 安装

`pip install --upgrade youtube-dl`

#### 用法

`youtube-dl "网址"`

### 1.9 tablib --各类表格数据处理工具

Tablib是一个格式无关的表格数据集库，用Python编写。它允许以pythonical方式导入、导出和操作表格数据集。高级功能包括隔离、动态列、标记/筛选和无缝格式导入/导出。
[项目地址](./tablib_env/README.md)

### 1.10 pdfminer --PDF文档信息提取工具

pdfminer侧重于获取和分析文本数据。Pdfminer.six 直接从页面中提取文本 PDF 的源代码。它还可用于获取文本的确切位置、字体或颜色。
[项目地址](./pdfminer_env/README.md)

### 1.11 pypdf2 --pdf拆分、合并、裁剪和转换工具

PyPDF2 是一个免费的开源纯 python PDF 库，能够拆分、合并、裁剪和转换PDF 文件的页面。它还可以添加 自定义数据、查看选项和 PDF 文件的密码。PyPDF2也可以从PDF中检索文本和元数据。
[项目地址](./pypdf2_env/README.md)

## 2. 相关领域类（财经、医疗、生物、化学、物理）

### 2.1 AKShare --基于 Python 的财经数据接口库

1. 目的是实现对股票、期货、期权、基金、外汇、债券、指数、加密货币等金融产品的基本面数据、实时和历史行情数据、衍生数据从数据采集、数据清洗到数据落地的一套工具。
2. Backtrader 是基于 Python 编程语言的主要用于量化投资开源回测和交易的框架，可以用于多种资产的回测。 目前，Backtrader 可以用于实现股票、期货、期权、外汇、加密货币等资产的回测，同时该开源框架也有强大的第三方社区支持，目前已经实现了 基于 IB、Oanda、VC、CCXT、MT5 等接口量化交易。
   [项目地址](./AKshare_env/README.md)

#### 安装

`pip install akshare  --upgrade`
`pip install backtrader`
`pip install matplotlib==3.2.2`

#### 使用前注意升级

`pip install akshare --upgrade -i https://pypi.org/simple`

### 2.2 Astropy --天文领域

[项目网址](https://www.astropy.org/)

### 2.3 biopython --python生物计算工具

[项目网址](https://biopython.org/)

### 2.4 cclib --用于解析和解释计算化学包的结果

[项目网址](http://cclib.github.io/index.html)
[openbabel-生物化学文件处理](http://openbabel.org/docs/current/)
[RDKit-开源化学信息学软件](http://www.rdkit.org/)

### 2.5 Obspy --处理地震数据的Python框架

[项目地址](./obspy_env/README.md)

#### 安装

`pip install obspy`

### 2.6 quTip --用于模拟开放量子系统动力学的开源库

[项目地址](./qutip_env/README.md)

## 3. 语音类

### 3.1 pyAudio_Analysis --用于音频特征提取、分类、分割和应用

[项目地址](./pyAudio_env/README.md)

#### 配置

```python
1. 环境
python37->pyAudio_env
2. 安装
git clone https://github.com/tyiannak/pyAudioAnalysis.git
pip install -r ./requirements.txt
pip install -e .
```

#### 使用

[音频处理方法](https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y)
未完待续...

## 4. 各类可视化画图库以及视觉方法总结

### 4.1 Seaborn 统计数据可视化

Seaborn是一个基于matplotlib的Python可视化库。它提供了一个高级界面，用于绘制有吸引力的统计图形。
[项目地址](./seaborn_env/README.md)

#### 1）配置

```python
1. 环境
python37->seaborn_env
2. 安装
pip install seaborn
```

#### 2）使用

[API示例](https://seaborn.pydata.org/examples/index.html)
[高质量绘图](https://seaborn.pydata.org/examples/grouped_boxplot.html)
未完待续...

### 4.2 Vega-Altair 声明式统计可视化库

除了绘制基本图像，Altair强大之处在于用户可以与图像进行交互，包括平移、缩放、选中某一块数据等操作。
[项目地址](./vega_env/README.md)

#### 1）配置

```python
1. 环境
python37->vega_env
2. 安装
pip install altair # 依赖
pip install vega_datasets # 内置数据库
```

#### 2）使用

[API示例](https://altair-viz.github.io/gallery/index.html)
[高质量绘图编码](https://altair-viz.github.io/user_guide/encoding.html)
未完待续...

### 4.3 bqplot --Jupyter 项目的交互式二维绘图库

bqplot是Jupyter的2D可视化系统，基于以下结构的图形语法。在 bqplot 中，绘图的每个组件都是一个交互式小部件。这允许 用户将可视化与其他Jupyter交互式小部件集成，以 使用几行 Python 代码创建集成的 GUI。

#### 1）配置

```python
1. 环境
python37->bqplot_env
2. 安装
第一种：
$ conda install -c conda-forge bqplot
第二种：
$ pip install bqplot
$ jupyter nbextension enable --py --sys-prefix bqplot
```

#### 2）使用

[API示例](https://bqplot.readthedocs.io/en/latest/api_documentation.html)
未完待续...

### 4.4 Cartopy --绘制地图

Cartopy旨在为数据制作绘图地图 分析和可视化.

#### 1）配置

安装失败，可能需要Linux环境

#### 2）使用

[API示例](https://blog.csdn.net/Jasenjane/article/details/125896265)

### 4.5 dash --在web上应用的python库用于画图

#### 1) 安装

pip install dash

#### 2) 说明

[项目地址](https://xercis.blog.csdn.net/article/details/107056777?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-107056777-blog-116558050.pc_relevant_multi_platform_whitelistv3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-107056777-blog-116558050.pc_relevant_multi_platform_whitelistv3&utm_relevant_index=8)

### 4.6 Kornia --基于PyTorch 的一个可微分的计算机视觉库。

[项目地址](./kornia_env/README.md)

#### 配置

```python
1. 环境
python37->kornia_env
2. 安装(包含torch)
pip install kornia
pip install kornia[x]  # to get the training API !
```

## 5. 信息安全类

### 5.1 gmssl以及pycryptodome

[项目地址](./gmssl_env/README.md)

#### 配置

```python
1. 环境
python37->gmssl_env
2. 安装
pip install gmssl
pip install pycryptodome
```

#### gmssl sm2,sm3,sm4

#### pycryptodome

#### cryptography

## 6. python GUI界面总结

### 6.1 [pyqt](https://zhuanlan.zhihu.com/p/162866700)

### 6.2

### [6.3 DearPyGui --一个易于使用、动态、GPU 加速的跨平台图形、 适用于 Python 的用户界面工具包](https://dearpygui.readthedocs.io/en/latest/index.html)

## 7. 机器学习方面

### 7.1 Magenta --机器学习用于创作艺术和音乐

[项目网址](https://github.com/magenta/magenta)
[博客和demo](https://magenta.tensorflow.org/)

## 8 django系统汇总

### 8.1 cartridge 购物车应用程序

#### 1) 安装

pip install -U cartridge

#### 2) 使用

mezzanine-project -a cartridge project_name
cd project_name
python manage.py createdb --noinput
python manage.py runserver

#### 3) 教程

[使用教程](https://blog.csdn.net/yanghuan313/article/details/70215655?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-70215655-blog-125327167.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-70215655-blog-125327167.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=5)

### 8.2 GeoDjango --基于django的地理web模块

[项目地址](https://docs.djangoproject.com/en/dev/ref/contrib/gis/)

## 9 游戏开发

### 9.1 Arcade 开发2D视频游戏

#### 1) 官方主页

[主页地址](https://api.arcade.academy/en/latest/)

#### 2) 游戏示例

[简单示例1](./Arcade_env/test.py)
[简单示例2](./Arcade_env/battle-bros-pyarcade/main.py)
[示例地址](https://api.arcade.academy/en/latest/sample_games.html)

### 9.2 Cocos2d C++版

[见C++开发](../C%2B%2B/Cocos2d/README.md)

### 9.3 harfang3d 3D 实时可视化工具

[文档](./harfang3d_env/README.md)

## 10 深度学习-NLP工具处理类

### 10.1 [gensim --NLP与信息检索相关](./gensim_env/README.md)

gensim读取一段语料，输出一个向量，表示文档中的一个词。可用于计算相似度。

### 10.2 [NLTK --用于文本分类、标记化、词干提取、标记、解析和语义推理](https://www.nltk.org/)

### 10.3 [pattern --Web挖掘模块](./pattern_env/README.md)

它具有数据挖掘工具（谷歌，推特和维基百科API，Web爬虫，HTML DOM解析器）、自然语言处理（词性标注、n-gram搜索，情感分析，WordNet），机器学习（向量空间模型，聚类，支持向量机）、网络分析和可视化。(库未识别)

### 10.4 [polyglot --传统nlp处理方法，多语言文本处理汇总](./polyglot_env/README.md)

### 10.5 [PyTorch-NLP --pytorch专用的NLP库](https://github.com/PetrochukM/PyTorch-NLP)

PyTorch-NLP是Python中自然语言处理（NLP）的库。它是用 考虑到最新的研究，并且从第一天起就设计用于支持快速原型设计。PyTorch-NLP 带有预先训练的嵌入、采样器、数据集加载器、指标、神经网络模块 和文本编码器。

## 11 深度学习-CV工具处理类

## 12 深度学习-数据集汇总类

### 12.1 [funNLP --史上最全的中文NLP语料库](https://github.com/fighting41love/funNLP)

## 13 深度学习-数据挖掘

### 13.1 [orange --开源的数据挖掘工具，采用Python+QT技术栈，可实现非监督学习、监督学习、频谱分析等应用场景](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#)

`可进行数据预处理、分类、回归、聚类、距离、评价等操作`

### 13.2 [chatgpt --GPT3.5](./chatgpt_env/README.md)

## 14 地理类

### 14.1 [GeoIP2 --提供 IP 地理定位和代理检测](https://github.com/maxmind/GeoIP2-python)

### 14.2 [GeoJSON --用于编码和解码GeoJSON格式数据](https://github.com/jazzband/geojson)

### 14.3 [GeoPy -- Python 客户端，用于定位 使用第三方的全球地址、城市、国家/地区和地标 地理编码器和其他数据源](https://geopy.readthedocs.io/en/latest/#)
