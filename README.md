# Ⅰ语言整理

## 1、 Python

| 主题                                                                                 | 详情                                                                                                                                                                                                                                                                                                                                                                         |
| :----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`01.初识Python`](./Python/Day01-15/01.初识Python.md)                                 | python环境安装                                                                                                                                                                                                                                                                                                                                                               |
| [`02.语言元素`](./Python/Day01-15/02.语言元素.md)                                     | type(),int(),float(),str(),chr(),ord(),运算符                                                                                                                                                                                                                                                                                                                                |
| [`03.分支结构`](./Python/Day01-15/03.分支结构.md)                                     | if                                                                                                                                                                                                                                                                                                                                                                           |
| [`04.循环结构`](./Python/Day01-15/04.循环结构.md)                                     | for,while,print('*',end='')不换行                                                                                                                                                                                                                                                                                                                                            |
| [`05.构造程序逻辑`](./Python/Day01-15/05.构造程序逻辑.md)                             | from random import randint                                                                                                                                                                                                                                                                                                                                                   |
| [`06.函数和模块的使用`](./Python/Day01-15/06.函数和模块的使用.md)                     | math库以及不同文件中函数模块的引用                                                                                                                                                                                                                                                                                                                                           |
| [`07.字符串和常用数据结构`](./Python/Day01-15/07.字符串和常用数据结构.md)             | 1.字符串(str)的各项操作(len,find),sys.getsizeof()检查内存,<br />2.列表(list=[*,*])的各项操作(enumerate,append,insert,remove,pop,clear,反向切片list[::-1],sort,生成器算法yield的使用),<br />3.元组(tuple=(*,*))的各项操作(与list相互转换,元组的元素不能修改),<br />4.集合(set={*,*})的各项操作(add,update,discard,pop),<br />5.字典(dict={*:*,*:*}):zip,get,popitem |
| [`08.面向对象编程基础`](./Python/Day01-15/08.面向对象编程基础.md)                     | 类class的定义,可见性问题(私有属性是以下划线开头)                                                                                                                                                                                                                                                                                                                             |
| [`09.面向对象进阶`](./Python/Day01-15/09.面向对象进阶.md)                             | @property装饰器(getter,setter),__slots__,静态方法@staticmethod和类方法@classmethod,继承和多态                                                                                                                                                                                                                                                                          |
| [`10.图形用户界面和游戏开发`](./Python/Day01-15/10.图形用户界面和游戏开发.md)         | 简单GUI的tkinter, 游戏开发pygame,panda3D                                                                                                                                                                                                                                                                                                                                     |
| [`11.文件和异常`](./Python/Day01-15/11.文件和异常.md)                                 | 文件操作(open,read,write),异常(try,excert,finally),读写json文件(dump,load),网络请求requests.get()                                                                                                                                                                                                                                                                            |
| [`12.字符串和正则表达式`](./Python/Day01-15/12.字符串和正则表达式.md)                 | import re (compile,match,search,split,sub)                                                                                                                                                                                                                                                                                                                                   |
| [`13.进程和线程`](./Python/Day01-15/13.进程和线程.md)                                 | 1.多进程 from multiprocessing import Process, Process(start,join), Queue<br />2.多线程 from threading import Thread,                                                                                                                                                                                                                                                         |
| [`14.网络编程入门和网络应用开发`](./Python/Day01-15/14.网络编程入门和网络应用开发.md) | 1.requests.get('http://****').json()<br /> 2.socket.(family='', type='').bind(IP,port) <br /> 3.服务端和客户端代码<br /> 4.网络应用开发(发送邮件,发送短信)                                                                                                                                                                                                                   |
| [`15.图像和办公文档处理`](./Python/Day01-15/15.图像和办公文档处理.md)                 | 1.PIL(剪裁,缩略,滤镜) 2.处理EXCEL和word                                                                                                                                                                                                                                                                                                                                      |
| [`16-20.Python语言进阶`](./Python/Day16-20/16-20.Python语言进阶.md)                   | 1.排序算法(选择、冒泡和归并)和查找算法(顺序和折半)<br /> 2.常用算法:穷举法,贪婪法,分治法,回溯法,动态规划 <br /> 3.filter,map,global和nonlocal,匿名函数和内联函数的用法(lambda函数)对象的复制,垃圾回收,循环引用和弱引用,面向对象设计原则solid <br /> 4.迭代器和生成器,并发编程                                                                                                |
| [`21-30.Web前端概述`](./Python/Day21-30/21-30.Web前端概述.md)                         | JQuery,vue,css等                                                                                                                                                                                                                                                                                                                                                             |
| [`31-35.玩转Linux操作系统`](./Python/Day31-35/31-35.玩转Linux操作系统.md)             | linux命令解析                                                                                                                                                                                                                                                                                                                                                                |
| [`36-*.数据库和机器学习`](./Python/other.md)                                          | 数据库和numpy,pandas,数据可视化,机器学习和深度学习                                                                                                                                                                                                                                                                                                                           |

## 2、 C++

### 2.1 基础进阶

| 主题                                                                          | 详情                                                                                                                                                                                                                        |
| :---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`const`](./C++/CPlusPlusThings/basic_content/const/README.md)                 | 1.指针与const(const *指向const常量的指针, * const常指针-指针本身是常量)及其赋值,<br /> 2.函数与const(返回值，参数) <br /> 3.类与const(const对象只能访问const成员函数,而非const对象可以访问任意的成员函数,包括const成员函数) |
| [`static`](./C++/CPlusPlusThings/basic_content/static/README.md)               | 1.函数中的静态变量(当变量声明为static时，空间将在程序的生命周期内分配)<br /> 2.类中的静态变量(由对象共享,不能使用构造函数初始化) <br /> 3.静态成员(类对象为静态-直到程序的生命周期,类中的静态函数-使用.或::来调用)          |
| [`this`](./C++/CPlusPlusThings/basic_content/this/README.md)                   | this指针(this在成员函数的开始执行前构造，在成员的执行结束后清除)                                                                                                                                                            |
| [`inline`](./C++/CPlusPlusThings/basic_content/inline/README.md)               | 1.类中内联(内联能提高函数效率-以代码复制为代价,省去了函数调用的开销)<br />2.inline virtual 唯一可以内联的是在编译器具有实际对象时                                                                                           |
| [`sizeof`](./C++/CPlusPlusThings/basic_content/sizeof/README.md)               | 类内大小的计算                                                                                                                                                                                                              |
| [`纯虚函数和抽象类`](./C++/CPlusPlusThings/basic_content/abstract/README.md)   | 1.纯虚函数(没有函数体的虚函数)<br />2.抽象类(包含纯虚函数的类)-抽象类只能作为基类来派生新类使用,不能创建抽象类的对象                                                                                                        |
| [`vptr_vtable`](./C++/CPlusPlusThings/basic_content/vptr_vtable/README.md)     | C++虚函数的vptr与vtable                                                                                                                                                                                                     |
| [`virtual`](./C++/CPlusPlusThings/basic_content/virtual/README.md)             | C++虚函数                                                                                                                                                                                                                   |
| [`volatile`](./C++/CPlusPlusThings/basic_content/volatile/README.md)           | (嵌入式开发)被volatile修饰的变量,读写时会引发一些可观测的副作用                                                                                                                                                             |
| [`assert`](./C++/CPlusPlusThings/basic_content/assert/README.md)               | 1.如果它的条件返回错误，则终止程序执行<br />2.#define NDEBUG 加上这行,则 assert 不可用                                                                                                                                      |
| [`位域`](./C++/CPlusPlusThings/basic_content/bit/README.md)                    | 位域bit的声明,初始化,大小和对齐                                                                                                                                                                                             |
| [`extern`](./C++/CPlusPlusThings/basic_content/extern/README.md)               | 1.C++调用C函数时,引用C的头文件时,需要加extern "C"{}<br />2.C调用C++函数(×)                                                                                                                                                 |
| [`struct`](./C++/CPlusPlusThings/basic_content/struct/README.md)               | 1.C中struct 2.C++中struct                                                                                                                                                                                                   |
| [`union`](./C++/CPlusPlusThings/basic_content/union/README.md)                 | 联合(union)是一种节省空间的特殊的类,一个 union 可以有多个数据成员,但是在任意时刻只有一个数据成员可以有值                                                                                                                    |
| [`c 实现 c++ 多态`](./C++/CPlusPlusThings/basic_content/c_poly/README.md)      | ***使用struct来模拟类                                                                                                                                                                                                       |
| [`explicit`](./C++/CPlusPlusThings/basic_content/explicit/README.md)           | 构造函数被explicit修饰后, 就不能再被隐式调用                                                                                                                                                                                |
| [`friend`](./C++/CPlusPlusThings/basic_content/friend/README.md)               | 1.友元函数(在类内声明,类外定义-可以在任何地方调用,友元函数中通过对象名来访问该类的私有或保护成员)<br />2.友元类(类B是类A的友元，那么类B可以直接访问A的私有成员)-无继承无传递                                                |
| [`using`](./C++/CPlusPlusThings/basic_content/using/README.md)                 | using声明(using declaration)是将命名空间中单个名字注入到当前作用域的机制,使得在当前作用域下访问另一个作用域下的成员时无需使用限定符::                                                                                       |
| [`::`](./C++/CPlusPlusThings/basic_content/maohao/README.md)                   | (::name)(class::name)(namespace::name)                                                                                                                                                                                      |
| [`enum`](./C++/CPlusPlusThings/basic_content/enum/README.md)                   | 使用枚举类来解决命名冲突问题 & 类中的枚举代替const                                                                                                                                                                          |
| [`decltype`](./C++/CPlusPlusThings/basic_content/decltype/README.md)           | decltype的作用是"查询表达式的类型"                                                                                                                                                                                          |
| [`引用与指针`](./C++/CPlusPlusThings/basic_content/pointer_refer/README.md)    | 1.引用: 必须初始化,不能为空,不能更换目标<br />2.指针:	可以不初始化,可以为空(使用指针的时候需要首先判断指针是否为空指针，否则可能会引起程序崩溃),可以更换目标                                                                |
| [`宏`](./C++/CPlusPlusThings/basic_content/macro/README.md)                    | 1.字符串化操作符(#)<br /> 2.符号连接操作符(##) <br /> 3.续行操作符(\)                                                                                                                                                       |
| [`函数重载`](./C++/CPlusPlusThings/basic_content/other/chongzai.md)            |                                                                                                                                                                                                                             |
| [`new和delete运算符`](./C++/CPlusPlusThings/basic_content/other/new_delete.md) |                                                                                                                                                                                                                             |
| [`类和对象`](./C++/CPlusPlusThings/basic_content/other/class.md)               |                                                                                                                                                                                                                             |
| [`类和对象plus`](./C++/CPlusPlusThings/basic_content/other/class.md)           |                                                                                                                                                                                                                             |
| [`继承与派生`](./C++/CPlusPlusThings/basic_content/other/jicheng.md)           |                                                                                                                                                                                                                             |
| [`多态性与虚函数`](./C++/CPlusPlusThings/basic_content/other/duotai.md)        |                                                                                                                                                                                                                             |
| [`函数模板与类模板`](./C++/CPlusPlusThings/basic_content/other/moban.md)       |                                                                                                                                                                                                                             |
| [`C++输入与输出`](./C++/CPlusPlusThings/basic_content/other/shuru.md)          |                                                                                                                                                                                                                             |

# Ⅱ paper

## 1、 PSPNET

### 1.1 模型介绍

改进的pspnet本质上是一个编码器解码器模型。整个训练过程如下：

1. 首先，将输入图像经过CNN网络进行下采样，得到一个Featuremap(这里主要是使用改进的Resnet网络，实现从图片到数字编码的过程)。(编码过程)
2. 将Featuremap接入pyramid parsing module(金字塔模型)，通过这个金字塔模块将图像编码层分为全局和层级局部(也就是多部分的局部)，并通过级联层以及各个卷据(CONV)操作形成最终的特征表示，使得编码结果同时携带图像的局部和全局上下文信息(这里主要是让网络获取更多的语义编码信息，致使后续语义分割效果更好)。
3. 最后，对上采样后的特征图进行像素点分类完成了整个语义分割过程。(解码过程)

# Ⅲ Experiment

# Ⅳ Project

## [Python项目汇总](./project/python/README.md)

### 虚拟环境配置

```python
virtualenv *_env
cd Scripts
./activate
```

### 虚拟环境进入

```py
1) conda activate python37
2) cd errbot_env/Scripts
3) ./activate
```

## 1. 项目工程类

### 1.1 [errbot 聊天机器人](./project/python/errbot/)

### 1.2 [pylama 代码审计工具](./project/python/pylama_env/README.md)

### 1.3 [fsociety 模块化渗透测试框架](./project/python/fsociety_env/README.md)

### 1.4 代码跟踪和分析工具

1. Hunter用于代码跟踪，不是用于测量覆盖率，而是用于调试，日志记录，检查和其他
   [Hunter项目网址](https://github.com/ionelmc/python-hunter)
2. Py-spy是Python程序的采样分析器
   [Py-spy项目网址](https://github.com/benfred/py-spy)

### 1.5 [psutil --进程监控和系统利用率管理工具](./project/python/psutil_env/README.md)

### 1.6 [barcode --条形码生成工具](./project/python/barcode_env/README.md)

### 1.7 [qrcode --二维码生成器工具](./project/python/qrcode_env/README.md)

### 1.8 [Youtube-dl --基于Python的下载视频的工具](./project/python/Youtube_env/README.md)

### 1.9 [tablib --各类表格数据处理工具](./project/python/tablib_env/README.md)

### 1.10 [pdfminer --PDF文档信息提取工具](./project/python/pdfminer_env/README.md)

### 1.11 [pypdf2 --pdf拆分、合并、裁剪和转换工具](./project/python/pypdf2_env/README.md)

## 2. 相关领域类（财经、医疗、生物、化学、物理）

### 2.1 [AKShare --基于 Python 的财经数据采集、清洗库](./project/python/AKshare_env/README.md)

### 2.2 [Astropy --天文领域工具](https://www.astropy.org/)

### 2.3 [biopython --python生物计算工具](https://biopython.org/)

### 2.4 [cclib --用于解析和解释计算化学包的结果](http://cclib.github.io/index.html)

[openbabel-生物化学文件处理](http://openbabel.org/docs/current/)
[RDKit-开源化学信息学软件](http://www.rdkit.org/)

### 2.5 [Obspy --处理地震数据的Python框架](./project/python/obspy_env/README.md)

### 2.6 [quTip --用于模拟开放量子系统动力学的开源库](./project/python/qutip_env/README.md)

## 3. 语音类

### 3.1 [pyAudio_Analysis --用于音频特征提取、分类、分割和应用](./project/python/pyAudio_env/README.md)

## 4. 各类可视化画图库以及视觉方法总结

### 4.1 [Seaborn 统计数据可视化](./project/python/seaborn_env/README.md)

### 4.2 [Vega-Altair 声明式统计可视化库-可与图像交互](./project/python/vega_env/README.md)

### 4.3 [bqplot --Jupyter 项目的交互式二维绘图库](https://bqplot.readthedocs.io/en/latest/api_documentation.html)

### 4.4 [Cartopy --绘制地图](https://blog.csdn.net/Jasenjane/article/details/125896265)

### 4.5 [dash --在web上应用的python库用于画图](https://xercis.blog.csdn.net/article/details/107056777?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-107056777-blog-116558050.pc_relevant_multi_platform_whitelistv3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-107056777-blog-116558050.pc_relevant_multi_platform_whitelistv3&utm_relevant_index=8)

### 4.6 [Kornia --基于PyTorch 的一个可微分的计算机视觉库](./project/python/kornia_env/README.md)

## 5. 信息安全类

### 5.1 [gmssl以及pycryptodome](./project/python/gmssl_env/README.md)

#### 包括gmssl sm2,sm3,sm4;pycryptodome;cryptography

## 6. python GUI界面总结

### 6.1 [pyqt](https://zhuanlan.zhihu.com/p/162866700)

### 6.2

### [6.3 DearPyGui --一个易于使用、动态、GPU 加速的跨平台图形、 适用于 Python 的用户界面工具包](https://dearpygui.readthedocs.io/en/latest/index.html)

## 7. 机器学习方面

### 7.1 [Magenta --机器学习用于创作艺术和音乐](https://github.com/magenta/magenta)

[博客和demo](https://magenta.tensorflow.org/)

## 8 django系统汇总

[Django大礼包--应用程序、项目和资源的精选表单](https://blog.csdn.net/m0_60142451/article/details/120709821?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-120709821-blog-120278787.pc_relevant_landingrelevant&spm=1001.2101.3001.4242.1&utm_relevant_index=3)

### 8.1 [cartridge 购物车应用程序](https://blog.csdn.net/yanghuan313/article/details/70215655?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-70215655-blog-125327167.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-70215655-blog-125327167.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=5)

### 8.2 [GeoDjango --基于django的地理web模块](https://docs.djangoproject.com/en/dev/ref/contrib/gis/)

## 9 游戏开发

### 9.1 [Arcade 开发2D视频游戏](https://api.arcade.academy/en/latest/)

https://api.arcade.academy/en/latest/sample_games.html)

### 9.2 Cocos2d C++版  [见C++开发](./project/C%2B%2B/Cocos2d/README.md)

### 9.3 [harfang3d 3D 实时可视化工具](./project/python/harfang3d_env/README.md)

## 10 深度学习-NLP工具处理类

### 10.1 [gensim --NLP与信息检索相关](./project/python/gensim_env/README.md)

### 10.2 [NLTK --用于文本分类、标记化、词干提取、标记、解析和语义推理](https://www.nltk.org/)

### 10.3 [pattern --Web挖掘模块](./project/python/pattern_env/README.md)

### 10.4 [polyglot --传统nlp处理方法，多语言文本处理汇总](./project/python/polyglot_env/README.md)

### 10.5 [PyTorch-NLP --pytorch专用的NLP库](https://github.com/PetrochukM/PyTorch-NLP)

## 11 深度学习-CV工具处理类

## 12 深度学习-数据集汇总类

### 12.1 [funNLP --史上最全的中文NLP语料库](https://github.com/fighting41love/funNLP)

## 13 深度学习-数据挖掘

### 13.1 [orange --开源的数据挖掘工具，采用Python+QT技术栈，可实现非监督学习、监督学习、频谱分析等应用场景](https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/#)

`可进行数据预处理、分类、回归、聚类、距离、评价等操作`

### 13.2 [chatgpt --GPT3.5](./project/python/chatgpt_env/README.md)

## 14 地理类

### 14.1 [GeoIP2 --提供 IP 地理定位和代理检测](https://github.com/maxmind/GeoIP2-python)

### 14.2 [GeoJSON --用于编码和解码GeoJSON格式数据](https://github.com/jazzband/geojson)

### 14.3 [GeoPy -- Python 客户端，用于定位 使用第三方的全球地址、城市、国家/地区和地标 地理编码器和其他数据源](https://geopy.readthedocs.io/en/latest/#)

## 2、C++

### 1. 标准库学习

[1.1 MyTinySTL](./project/C%2B%2B/MyTinySTL/learning.md)

### 2. web服务器学习

[2.1 TinyWebServer](./project/C%2B%2B/TinyWebServer/learning.md)

### 3. 游戏开发

#### 3.1 Cocos2d-x

[3.1 Cocos2d](./project/C%2B%2B/Cocos2d/README.md)
