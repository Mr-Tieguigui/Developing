# gensim使用
从宏观来看，gensim提供了一个发现文档语义结构的工具，通过检查词出现的频率。gensim读取一段语料，输出一个向量，表示文档中的一个词。词向量可以用来训练各种分类器模型。这三个模型是理解gensim的核心概念，所以接下来依次介绍。同时，会以一个简单例子贯穿讲述。

## 文集：
将原始的文档处理后生成语料库
```py
from gensim import corpora
import jieba
documents = ['工业互联网平台的核心技术是什么',
            '工业现场生产过程优化场景有哪些']
def word_cut(doc):
    seg = [jieba.lcut(w) for w in doc]
    return seg

texts= word_cut(documents)

## 为语料库中出现的所有单词分配了一个唯一的整数id
dictionary = corpora.Dictionary(texts)
dictionary.token2id
from gensim import corpora
import jieba
documents = ['工业互联网平台的核心技术是什么',
            '工业现场生产过程优化场景有哪些']
def word_cut(doc):
    seg = [jieba.lcut(w) for w in doc]
    return seg

texts= word_cut(documents)

## 为语料库中出现的所有单词分配了一个唯一的整数id
dictionary = corpora.Dictionary(texts)
dictionary.token2id

## 输出结果为：
{'互联网': 0,
 '什么': 1,
 '优化': 7,
 '哪些': 8,
 '场景': 9,
 '工业': 2,
 '平台': 3,
 '是': 4,
 '有': 10,
 '核心技术': 5,
 '现场': 11,
 '生产': 12,
 '的': 6,
 '过程': 13}
```

## 向量

把文档表示成向量
```py
## 该函数doc2bow()只计算每个不同单词的出现次数，将单词转换为整数单词id，并将结果作为稀疏向量返回
bow_corpus = [dictionary.doc2bow(text) for text in texts]
bow_corpus 

## 输出结果为：
[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)],
 [(2, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)]]
每个元组的第一项对应词典中符号的 ID，第二项对应该符号出现的次数。
```


## 模型
```py
from gensim import models
# train the model
tfidf = models.TfidfModel(bow_corpus)
```

### 一、分词

#### 分词工具

1. python︱六款中文分词模块尝试:jieba、THULAC、SnowNLP、pynlpir、CoreNLP、pyLTP

2. Hanlp

首先要对句子进行初步处理。本文对文本依次进行了【去空去重、切词分词和停用词过滤】操作。
原始数据会存在一些【空或重复的语句】，须过滤掉这些【无价值且影响效率】的语句。使用计算机自动地对中文文本进行词语切分的过程称为中文分词(Chinese Word Segmentation)，即使中文句子中的词之间有空格标识。若要对一个句子进行分析，就需要将其切分成词的序列，然后以词为单位进行句子的分析，故中文分词是中文自然语言处理中最基本的一个环节。

#### 生成分词列表

1. 首先停用词过滤，返回一个停用词表
可以使用中科院的“计算所汉语词性标记集”以及哈工大停用词表
```py
def StopWordsList(filepath):
    wlst = [w.strip() for w in open(filepath,'r',encoding='utf8').readlines()]
    return wlst
```

2、结巴分词后的停用词性 [标点符号、连词、助词、副词、介词、时语素、‘的’、数词、方位词、代词]
```[y]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
```

#### 对文本集中的文本进行中文分词，返回分词列表
```py
def seg_sentence(sentence,stop_words):
    sentence_seged = jieba.cut(sentence.strip())
    # sentence_seged = set(sentence_seged)
    outstr = ''
    for word in sentence_seged:
        if word not in stop_words:
            if word != '\t':
                outstr += word
                outstr += ' '

    return outstr.split(' ')
```

### 二、 基于文本集建立词典，计算相似度##
```py
        #1、将【文本集】生产【分词列表】
    texts = [seg_sentence(seg,stop_words) for seg in open(tpath,'r',encoding='utf8').readlines()]
    #一、建立词袋模型
        #2、基于文件集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(texts)
    feature_cnt = len(dictionary.token2id.keys())
        #3、基于词典，将【分词列表集】转换为【稀疏向量集】，也就是【语料库】
    corpus = [dictionary.doc2bow(text) for text in texts]
    #二、建立TF-IDF模型
        #4、使用“TF-TDF模型”处理【语料库】
    tfidf = models.TfidfModel(corpus)
    #三构建一个query文本，利用词袋模型的字典将其映射到向量空间    
        #5、同理，用词典把搜索词也转换为稀疏向量
    kw_vector = dictionary.doc2bow(seg_sentence(keyword,stop_words))
        #6、对稀疏向量建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=feature_cnt)
        #7、相似的计算
    sim = index[tfidf[kw_vector]]
```

