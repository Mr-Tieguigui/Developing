


import jieba
import jieba.posseg as pseg
from gensim import corpora, models, similarities

def StopWordsList(filepath):
    wlst = [w.strip() for w in open(filepath, 'r', encoding='utf8').readlines()]
    return wlst


def seg_sentence(sentence, stop_words):
    # stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']#过滤数字m
    stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'f', 'r']
    sentence_seged = pseg.cut(sentence)
    # sentence_seged = set(sentence_seged)
    outstr = []
    for word,flag in sentence_seged:
        # if word not in stop_words:
        if word not in stop_words and flag not in stop_flag:
            outstr.append(word)
    return outstr


if __name__ == '__main__':
    spPath = 'stopwords.txt'
    tpath = 'test.txt'
  
    stop_words = StopWordsList(spPath)
    keyword = '吃鸡'

    # 1、将【文本集】生产【分词列表】
    texts = [seg_sentence(seg, stop_words) for seg in open(tpath, 'r', encoding='utf8').readlines()]
    orig_txt = [seg for seg in open(tpath, 'r', encoding='utf8').readlines()]

#一、建立词袋模型
    # 2、基于文件集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(texts)
    feature_cnt = len(dictionary.token2id.keys())
    # 3、基于词典，将【分词列表集】转换为【稀疏向量集】，也就是【语料库】
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 4、使用“TF-TDF模型”处理【语料库】
#二、建立TF-IDF模型
    tfidf = models.TfidfModel(corpus)
#三构建一个query文本，利用词袋模型的字典将其映射到向量空间
    # 5、同理，用词典把搜索词也转换为稀疏向量
    kw_vector = dictionary.doc2bow(seg_sentence(keyword, stop_words))
    # 6、对稀疏向量建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    # 7、相似的计算
    sim = index[tfidf[kw_vector]]

    result_list = []
    for i in range(len(sim)):
        print('keyword 与 text%d 相似度为：%.2f' % (i + 1, sim[i]))
        if sim[i] > 0.4:
            result_list.append(orig_txt[i])

    print('原始的句子：',result_list)