# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     regular
   Description :
   Author :       7326
   date：          2017/12/22
-------------------------------------------------
   Change Activity: 2017/12/22
-------------------------------------------------
"""
__author__ = '7326'

'''
正则表达式
结巴分词

'''



# 结巴分词
import jieba

def fun():

    seg_list = jieba.cut("我在学习自然语言处理",cut_all=True)
    print(seg_list)
    print("Full Mode:"+ '/'.join(seg_list))     #全模式
    seg_list = jieba.cut("我在学习自然语言处理",cut_all=False)
    print(seg_list)
    print("Default Mode:" + '/'.join(seg_list)) #精确模式


    seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")   #精确模式
    print(','.join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后再哈佛大学深造") # 所搜引擎模式
    print(','.join(seg_list))

    # 直接返回list
    print(jieba.lcut("他毕业于上海交通大学，在百度深度学习研究院进行研究"))
    print(','.join(jieba.lcut("他毕业于上海交通大学，在百度深度学习研究院进行研究")))



'''
自定义词典
'''
def fun1():


    # 添加词典
    jieba.add_word()



    # HMM 隐式马尔可夫
    print('/'.join(jieba.cut("如果放到旧字典中将出错",HMM=False)))
    # 动态分割
    jieba.suggest_freq(("中","将"),True)
    print('/'.join(jieba.cut("如果放到旧字典中将出错",HMM=False)))


'''
关键词提取
def extract_tags(sentence, topK=20, withWeight=False, allowPOS=(), withFlag=False):
- sentence: 待提取的文本
- topK: return how many top keywords. `None` for all possible words.
- withWeight: if True, return a list of (word, weight);
              if False, return a list of words.
- allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v','nr'].
            if the POS of w is not in this list,it will be filtered.
- withFlag: only work with allowPOS is not empty.
            if True, return a list of pair(word, weight) like posseg.cut
            if False, return a list of words
'''
import jieba.analyse as analyse

def fun2():

    lines = open('111.txt').read()
    print(' '.join(analyse.extract_tags(lines,topK=20,withWeight=False,allowPOS=())))



if __name__ == '__main__':
    fun2()
