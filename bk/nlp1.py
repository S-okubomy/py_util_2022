import sys
import re
import mylib
from mylib.mc.op_list import li
import datetime
import numpy as np
from numpy import linalg as lg
from janome.tokenizer import Tokenizer

sys.setrecursionlimit(2000)

def run():
    next_word_dic = get_next_word()
    sentence = ""
    first_word = "what"
    new_sen = get_sentence(next_word_dic, first_word, sentence)
    #print(new_sen)


def get_dic(st_lst):
    dic_set = set()
    li(st_lst).map(lambda s: dic_set.add(s))
    
    dic_set_sort = sorted(dic_set, reverse=False)
    print(dic_set_sort)

    dic = {}
    for i, x in enumerate(dic_set_sort):
        dic[x] = i + 1

    print(dic)

    return dic


def tmp1():
    st_data = "こんにちは。今日も暑いです。熱中症に気を付けます。\
            熱中症を防ぐにはどうしたら良いですか？ 睡眠と水分を十分取ります。"
    st_data += "方法はいくつかあります。良い方法を教えます。睡眠が大事です。 \
    快適な温度を教えてください。エアコンは25度が快適です。 場所を教えてください。東京です。\
     "
    que = "快適なエアコンの温度は何度ですか？"

    t = Tokenizer()
    st_lst = get_wakachi(t, st_data)

    dic = get_dic(st_lst)
    d, m = get_np(st_lst, dic)

    len_i, len_j = d.shape
    print(len_i, len_j)
    d_map = {}
    for i in range(len_i):
        d_map[i] = (d[i], m[i])

    sentence = get_sentence(dic,"", que, d_map, t)
    print(sentence)

def get_wakachi(t, st_data):
    return [token.surface for token in t.tokenize(st_data) if not token.surface.isspace()]

def get_next_word(dic, prev_sentence, d_map, t):
    len_w = len(d_map[0][0])
    print(prev_sentence)
    cnv_arr = li(get_wakachi(t, prev_sentence)).map(lambda s: dic.get(s) if dic.get(s) != None else 0).list
    trg = np.array(zero_ume(cnv_arr, len_w))
    print(trg)
    cos_sort_lst = get_cos_sort(trg, d_map)
    next_val = cos_sort_lst[0][0]
    next_word = inv_dic(dic).get(next_val)
    #print(f'{next_val} : {next_word}')
    return next_word


def get_cos_sort(trg, d_map):
    lst = []
    for (k,v) in d_map.items():
        #print(v)
        cos_val = cos_sim(trg, v[0])
        lst.append((int(v[1]), cos_val))

    lst.sort(key = lambda x: x[1], reverse=True)
    return lst        


def get_sentence(dic, sentence, cur_word, d_map, t):
    sentence +=  cur_word
    next_word = get_next_word(dic, sentence, d_map, t)
    if next_word == "。" or len(sentence) > 500:
        return sentence + "。"

    return get_sentence(dic, sentence, next_word, d_map, t)

def cos_sim(v1, v2):
    return v1 @ v2 / (lg.norm(v1) * lg.norm(v2))

def aten():
    # what is -> your
    # water is -> important
    
    # what is your -> favorit
    # water is important -> .
    # (-1) what is -> your
    pass

def div_data(words):
    lds = words[0:-1]
    mds = words[-1]
    return (lds, mds)

def zero_ume(arr, len_w):
    arr.extend([0 for _ in range(len(arr),len_w)])
    return arr

def inv_dic(dic):
    return { v:k for k,v in dic.items() } 


def get_np(st_lst, dic):
    cnv_lst = li(st_lst).map(lambda s : dic.get(s)).list
    print(cnv_lst)


    len_w = len(cnv_lst)
    d_arr = np.empty((0,len_w), dtype=int)
    m_arr = np.array([])
    len_date = len(cnv_lst)
    for start_ind in range(0,len_date):
        for end_ind in range(start_ind+1, len_date):
            d, m = div_data(cnv_lst[start_ind:end_ind+1])
            dn = np.array([zero_ume(d, len_w)])
            d_arr = np.append(d_arr,dn, axis=0)
            m_arr = np.append(m_arr,m)
            # print(f'{d} : {m}')
    
    return (d_arr, m_arr)


if __name__ == '__main__':
    #run()
    tmp1()
    
