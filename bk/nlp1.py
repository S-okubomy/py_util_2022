import sys
import re
import mylib
from mylib.mc.op_list import li
import datetime
import numpy as np
from numpy import linalg as lg

sys.setrecursionlimit(2000)

def run():
    next_word_dic = get_next_word()
    sentence = ""
    first_word = "what"
    new_sen = get_sentence(next_word_dic, first_word, sentence)
    #print(new_sen)


def get_dic(st_data):
    dic_set = set()
    li(st_data.split(" ")).map(lambda s: dic_set.add(s))
    
    dic_set_sort = sorted(dic_set, reverse=False)
    print(dic_set_sort)

    dic = {}
    for i, x in enumerate(dic_set_sort):
        dic[x] = i + 1

    print(dic)

    return dic


def tmp1():
    st_data = "what is important ? test is important . what is your favorit ? i like meal . what is important ? water is important ."
    X_st_data = "Outside the window on the 50th floor of the Shinjuku Nomura \
    Building is the night view of Shinjuku buildings . The twinkling lights as \
    far as the eye can see are so enchantingly beautiful that it is as if you \
    have wandered into the stars. The restaurant offers a variety of \
    gastronomic delights that combine the quintessential techniques of \
    traditional Japanese cuisine with carefully selected ingredients from all \
    over Japan . We will create a wonderful atmosphere for your special \
    occasion , such as an anniversary , celebration , or marriage proposal. "


    dic = get_dic(st_data)
    d, m = get_np(st_data, dic)

    len_i, len_j = d.shape
    print(len_i, len_j)
    d_map = {}
    for i in range(len_i):
        d_map[i] = (d[i], m[i])

    sentence = get_sentence(dic,"", "what is your favorit ?", d_map)
    print(sentence)

def get_next_word(dic, prev_sentence, d_map):
    len_w = len(d_map[0][0])
    print(prev_sentence)
    cnv_arr = li(prev_sentence.strip().split(" ")).map(lambda s: dic.get(s)).list
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


def get_sentence(dic, sentence, cur_word, d_map):
    sentence +=  cur_word + " "
    next_word = get_next_word(dic, sentence, d_map)
    if next_word == "." or len(sentence) > 500:
        return sentence + "."

    return get_sentence(dic, sentence, next_word, d_map)

def X_get_next_word(dic, prev_word, w):
    cnv_arr = li(prev_word.split(" ")).map(lambda s: dic.get(s)).list
    x = np.array(zero_ume(cnv_arr,10))
    print(x)
    next_val = (x @ w)[0]
    next_word = inv_dic(dic).get(round(next_val))
    print(f'{next_val} : {next_word}')
    return next_word

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
    #words = li(sentence.split(" ")).map(lambda s: dic.get(s)).list
    lds = words[0:-1]
    #lds.extend(words[0:-1])
    mds = words[-1]
    #for _ in range(len(lds), w_len):
    #    lds.append(0)
    return (lds, mds)

def zero_ume(arr, len_w):
    arr.extend([0 for _ in range(len(arr),len_w)])
    return arr

def inv_dic(dic):
    return { v:k for k,v in dic.items() } 


def get_np(st_data, dic):
    cnv_lst = li(st_data.split(" ")).map(lambda s : dic.get(s)).list
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


def X_get_np():
    lst = ["what is important ? test is important .", "what is your favorit ? i like meal .", "what is important ? water is important .", "what is your favorit meal .", "what is your favorit water" ]
    dic = { "what":1, "important":2, "is":3, "test":4, "meal":5, "water":6, "?":7, ".":8, "your":9, "favorit":10, "i":11, "like":12 }
    cnv_lst = li(lst).map(lambda s: li(s.split(" ")).map(lambda ss: dic.get(ss)).list).list
  
    print(cnv_lst)
    #print(div_data(dic, "what is important ? test", 10))

    all_word_len = li(lst).reduce(lambda acu, cur, i, arr: acu + len(arr), 0).val
    print(all_word_len)
    
    d_arr = np.empty((0, 10), dtype=int)
    m_arr = np.array([])
    s_map = {}
    for arr in cnv_lst:
        for i in range(1,len(arr)):
            d, m = div_data(arr[0:i+1])
            # print(zero_ume(d, 10))
            dn = np.array([zero_ume(d, 10)])
            d_arr = np.append(d_arr,dn, axis=0)
            m_arr = np.append(m_arr,m)
            #s_map[d] = m
            print(f'{d} : {m}') 

    print(s_map)
    return (d_arr, m_arr)

def X_get_next_word():
    lst = ["what is important ? test is important .", "what is your favorit ? i like meal .", "what is important ? water is important .", "what is your favorit meal .", "what is your favorit water" ]
    dic = { "what":1, "important":2, "is":3, "test":4, "meal":5, "water":6, "?":7, ".":8, "your":9, "favorit":10, "i":11, "like":12 }
    cnv_lst = li(lst).map(lambda s: li(s.split(" ")).map(lambda ss: dic.get(ss)).list).list
  
    print(cnv_lst)
    #print(div_data(dic, "what is important ? test", 10))

    all_word_len = li(lst).reduce(lambda acu, cur, i, arr: acu + len(arr), 0).val
    print(all_word_len)
    
    d_lst = []
    m_lst = []
    for arr in cnv_lst:
        for i in range(1,len(arr)):
            d, m = div_data(arr[0:i+1])
            # print(zero_ume(d, 10))
            d_lst.append(d)
            m_lst.append(m)

 
    return {"test":1}



if __name__ == '__main__':
    #run()
    tmp1()
    
