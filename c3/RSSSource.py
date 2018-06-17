import jieba.posseg
import feedparser

import re


# 从RRS源中获取单词出现次数统计
def get_word_counts(url):
    # 解析url
    d = feedparser.parse(url)
    wc = {}

    # 获取文本
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # 获取单词
        words = get_words(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    return d.feed.title, wc


def get_words(html):
    # 去除html标记
    txt = re.compile(r'<[^>]+>').sub('', html)

    # 利用分词器进行中文分词
    result = jieba.posseg.cut(txt)
    # words = jieba.cut(txt, cut_all=True)
    # words = jieba.cut_for_search(txt)n
    # words = jieba.analyse.extract_tags(txt, 100)

    # 去除空字符串，只选用名词
    return [item.word for item in result if item.flag[0] == 'n']


def build():
    ap_count = {}
    word_counts = {}
    url_list = [line for line in open('RSSUrl')]
    url_num = len(url_list)

    for url in url_list:
        try:
            title, wc = get_word_counts(url)
            word_counts[title] = wc
            for word, count in wc.items():
                ap_count.setdefault(word, 0)
                if count > 1:
                    ap_count[word] += 1
        except:
            print('解析URL数据失败 %s' % url)

    word_list = []
    for w, bc in ap_count.items():
        rate = float(bc) / url_num
        if rate > 0.3 < rate < 0.8:
            word_list.append(w)
            print(bc, w, "\n")

    # 将数据写入文件中
    out = open('data.txt', 'w')

    for word in word_list:
        out.write('\t' + word)

    out.write('\n')

    for blog, wc in word_counts.items():
        out.write(blog)
        for word in word_list:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')


if __name__ == '__main__':
    build()
