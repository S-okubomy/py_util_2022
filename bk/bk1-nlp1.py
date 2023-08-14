import sys
import re
import mylib
from mylib.mc.op_list import li
import datetime
import numpy as np

sys.setrecursionlimit(2000)

def run():
    next_word_dic = get_next_word()
    #print(f'next_word: {next_word_dic}')
    #print("test")
    sentence = ""
    first_word = "what"
    new_sen = get_sentence(next_word_dic, first_word, sentence)
    #print(new_sen)

def get_sentence(next_word_dic, word, sentence):
    sentence += " " + word
    next_word = next_word_dic.get(word)
    #print(next_word, sentence)
    if next_word == "test":
        return sentence
   
    # sentence += " " + next_word
    return get_sentence(next_word_dic, next_word, sentence) 


def aten():
    # what is -> your
    # water is -> important
    
    # what is your -> favorit
    # water is important -> .
    # (-1) what is -> your
    pass

def div_data(dic, words, w_len, ind_start):
    #words = li(sentence.split(" ")).map(lambda s: dic.get(s)).list
    lds = [0 for i in range(ind_start-1)]
    lds.extend(words[0:-1])
    mds = words[-1]
    for _ in range(len(lds), w_len):
        lds.append(0)
    return (lds, mds)

def inv_dic(dic):
    return { v:k for k,v in dic.items() } 

def get_next_word():
    lst = ["what is important ? test is important .", "what is your favorit ? i like meal .", "what is important ? water is important .", "what is your favorit meal .", "what is yor favorit water" ]
    dic = { "what":1, "important":2, "is":3, "test":4, "meal":5, "water":6, "?":7, ".":8, "your":9, "favorit":10, "i":11, "like":12 }
    cnv_lst = li(lst).map(lambda s: li(s.split(" ")).map(lambda ss: dic.get(ss)).list).list
  
    print(cnv_lst)
    #print(div_data(dic, "what is important ? test", 10))

    all_word_len = li(lst).reduce(lambda acu, cur, i, arr: acu + len(arr), 0).val
    print(all_word_len)
    
    ind_start = 0;
    for arr in cnv_lst:
        for i in range(1,len(arr)):
            print(div_data(dic, arr[0:i+1], all_word_len, ind_start))
        ind_start += len(arr)



    #all_cnt_lst = []
    #dic_max = {}
    #for k1,v1 in dic.items():
    #    cnt_lst = [0 for i in range(len(dic)+1)]
    #    cnt = 0;
    #    for k2,v2 in dic.items():
    #        for lst in cnv_lst:
    #            for i in range(len(dic)):
    #                if i+2 > len(lst):
    #                    continue
    #      
    #                if lst[i] == v1 and lst[i+1] == v2:
    #                    cnt_lst[v2] += 1

    #    #print(k1, cnt_lst)
    #    max_ind = li(cnt_lst).reduce(lambda acu, cur, i, arr: i if arr[acu] < cur else acu, 0).val
    #    #print(k1, max_ind)
    #    #print(k1, inv_dic(dic).get(max_ind))
    #    dic_max[k1] = inv_dic(dic).get(max_ind)
    #    all_cnt_lst.append(cnt_lst)

    #print(all_cnt_lst)
    #print(dic_max)
 
    return {"test":1}



if __name__ == '__main__':
    run()
    
