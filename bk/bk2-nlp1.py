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
    #print(st_lst)
    dic_set = set()
    li(st_lst).map(lambda s: dic_set.add(s))
    
    dic_set_sort = sorted(dic_set, reverse=False)
    #dic_set_sort = dic_set
    print(dic_set_sort)

    dic = {}
    for i, x in enumerate(dic_set_sort):
        dic[x] = i + 1

    print(dic)

    return dic


def tmp1():
    st_data = li().read("./st_data.txt").val
    print(f'st_data: {st_data}')

    #que = "確認はどうしたら良いですか？"
    que = "熱中症を防ぐにはどうしたら良いですか？"

    t = Tokenizer()
    st_lst = get_wakachi(t, st_data)

    dic = get_dic(st_lst)
    d, m = get_np(st_lst, dic)

    len_i, len_j = d.shape
    #print(len_i, len_j)
    d_map = {}
    for i in range(len_i):
        d_map[i] = (d[i], m[i])

    sentence = get_sentence(dic,"", que, d_map, t)
    print(sentence)

def get_wakachi(t, st_data):
    # return [token.surface for token in t.tokenize(st_data) if not token.surface.isspace()]
    return [token.surface for token in t.tokenize(st_data)]

def get_fixed_len_lst(arr, len_trg, ind_end):
    return arr[ind_end-len_trg if ind_end-len_trg >=0 else 0 : ind_end]

def get_next_word(dic, prev_sentence, d_map, t):
    len_w = len(d_map[0][0])
    print(prev_sentence)
    #cnv_arr = li(get_wakachi(t, prev_sentence + "")).map(lambda s: dic.get(s) if dic.get(s) != None else 0).filter(lambda s: s != 0).list
    #print(dic)
    waka = get_wakachi(t, prev_sentence)
    cnv_arr = li(get_wakachi(t, prev_sentence + "")).map(lambda s: dic.get(s) if dic.get(s) != None else 0).list
    if re.match("^(.|\s)* $", prev_sentence) != None:
        cnv_arr.append(dic.get(' '))

    if re.match("^.*\n $", prev_sentence) != None:
        cnv_arr.append(dic.get('\n '))

    if re.match("^(.|\s)*?\n$", prev_sentence) != None:
        cnv_arr.append(dic.get('\n'))

    print(f'waka: {waka}')
    print(f'cnv: {cnv_arr}')

    ind_end = len(cnv_arr)
    #trg = np.array(zero_ume(get_fixed_len_lst(cnv_arr, len_w, ind_end), len_w))
    trg = np.array(get_fixed_len_lst(cnv_arr, len_w, ind_end))
    #print(trg)
    cos_sort_lst = get_cos_sort(trg, d_map)

    if len(cos_sort_lst) == 0:
        return "end"

    next_val = cos_sort_lst[0][0]
    
    print(f'bst: {cos_sort_lst[0][2]}') 
    print(f'cos: {cos_sort_lst[0][1]}')
   
    next_word = inv_dic(dic).get(next_val)
    print(f'{next_val} : {next_word}')
    return next_word


def get_cos_sort(trg, d_map):
    lst = []
    print(f'trg: {trg}')
    len_trg = len(trg)
    for (k,v) in d_map.items():
        len_d = len(v[0])
        if len_trg >= len(v[0]) or v[0][len_trg] == 0:
            continue

        cos_val = cos_sim(trg, v[0][:len_trg])
        if cos_val > 0.0:
            lst.append((int(v[0][len_trg]), cos_val, v[0][:len_trg]))
        #lst.append((int(v[1]), cos_val))

    lst.sort(key = lambda x: x[1], reverse=True)
    return lst        

def get_sentence(dic, sentence, cur_word, d_map, t):
    print(f'cur_word: {cur_word}')
    if cur_word == None:
        return sentence + "。"

    sentence +=  cur_word
    next_word = get_next_word(dic, sentence, d_map, t)
    if next_word == "end" or next_word == "XXXXXX" or len(sentence) > 500:
        return sentence + "。"

    return get_sentence(dic, sentence, next_word, d_map, t)

def cos_sim(v1, v2):
    return v1 @ v2 / (lg.norm(v1) * lg.norm(v2))

def div_data(words):
    #lds = words[0:-1]
    #mds = words[-1]
    return (words, 0)

def zero_ume(arr, len_w):
    arr.extend([0 for _ in range(len(arr),len_w)])
    return arr

def inv_dic(dic):
    return { v:k for k,v in dic.items() } 


def get_np(st_lst, dic):
    cnv_lst = li(st_lst).map(lambda s : dic.get(s)).list
    print(cnv_lst)

    len_w = 50  # 特徴量の配列長さ
    d_arr = np.empty((0,len_w), dtype=int)
    m_arr = np.array([])
    len_date = len(cnv_lst)
    for end in range(2,len_date+len_w):
        d, m = div_data(get_fixed_len_lst(cnv_lst, len_w, end))
        dn = np.array([zero_ume(d, len_w)])
        #dn = np.array([d])
        d_arr = np.append(d_arr,dn, axis=0)
        m_arr = np.append(m_arr,m)
        # print(f'{d} : {m}')
    
    return (d_arr, m_arr)


if __name__ == '__main__':
    #run()
    tmp1()
    
