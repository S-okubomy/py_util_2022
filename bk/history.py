import datetime
import pytz
now_jp = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
now_jp
now_jp.hour
now_jp.month
.exit
quit()
quit
quit()
500 / 7
500 % 7
5 // 7
7 // 7
5 // 4
7 // 4
600 // 7
500 // 7
6 // 3
8 // 3
7 // 3
6 // 3
for i in range(1):
	print("test")
for i in range(0):
	print("test")
1 % 10
2 % 10
11 % 10
111 % 10
113 % 10
113 //  10
113 % 100
111 % 2
121 % 2
120 % 2
120 % 4
110 % 4
110 % 2
111 % 2
110 % 2
110 % 4
9%10
.exit
quit()
0 % 10
12 % 10
56 % 10
12 % 11
100 % 11
50 % 11
1 /2 % 11
1 //2 % 11
1 //2 
8/3
8/3 % 11
quit()
# import：import itertolls
import itertools
 
N,K=4,2
 
# 順列：permutations(range(N))
# seq=(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),...,(3,2,1,0)
print("[順列]")
for seq in itertools.permutations(range(N)):
    print(seq)
 
# 重複なしの組み合わせ：combinations(range(N),K)
print("[重複なしの組み合わせ]")
# seq=(0,1),(0,2),(0,3),(1,2)...,(2,3)
for seq in itertools.combinations(range(N),K):
    print(seq)
 
# 重複ありの組み合わせ：combinations_with_rep(range(N),K)
print("[重複ありの組み合わせ]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,1)...,(3,3)
for seq in itertools.combinations_with_replacement(range(N),K):
    print(seq)
 
# 直積：product(range(N),range(N)):
print("[直積]")
# seq=(0,0),(0,1),(0,2),(0,3),(1,0)...,(3,3)
for seq in itertools.product(range(N),range(N)):
    print(seq)
print("[順列]")
for seq in itertools.permutations(range(N)):
    print(seq)
print("[重複なしの組み合わせ]")
for seq in itertools.combinations(range(N),K):
    print(seq)
quit()
8 * 108
8 * 108 / 100
100000000
2**60
10**9
sqrt(8)
import math
math.sqrt(8)
math.sqrt(3)
math.sqrt(9)
math.sqrt(12)
2 % 2
33 % 88
quit()
6!
def fact(x):
	if x == 0 || x == 1: 
def fact(x):
	if x == 0 or x == 1: 
		return x
	x * fact(x-1)
fact(3)
6*2
def fact(x):
	if x == 0 or x == 1: 
		return 1
	x*fact(x-1)
fac(5)
fact(5)
def fact(x):
	if x == 0 or x == 1: 
		return 1
	return x*fact(x-1)
fact(3)
fact(7)
fact(5)
fact(2*10**5)
fact(10**5)
fact(10**2)
2**31
2**32
1<< 2
1<< 0
1 << 1
log1
math.log10
import math
math.log2(2)
10* math.log(10) / math.log(2)
10**9
2000/11
120*14
2000/14
2000/15
2000/16
2000/17
2**12
6**4
2**6
quit()
(1+1000000000)/2
(1+1000000000)//2
2**20
10**9
2**40
quit
quit()
2 % 5
5 % 2
quit()
import pandas as pd
quit()
import pandas as pd
s1 = pd.Series([1,2,3,5])
print(s1)
df = pd.read_csv(sys.stdin)
import sys
df = pd.read_csv(sys.stdin)
print(df)
df = pd.read_csv(sys.stdin)
print(df)
df = pd.read_csv(sys.stdin)
print(df)
df = pd.read_table(sys.stdin)
print(df)
df = pd.read_table(sys.stdin)
df = pd.read(sys.stdin)
df = pd.read_spss(sys.stdin)
df = pd.read_clipboard()
df = pd.read_fwf(sys.stdin)
print(df)
df.info
df.info()
len(df.columns)
df = pd.read_fwf(sys.stdin, header=none)
df = pd.read_fwf(sys.stdin, header=None)
print(df)
len(df.columns)
li = 
pd.Series(sys.stdin.read())
s = pd.Series(sys.stdin.read())
s
len(s)
print(s)
s = pd.Series(sys.stdin.read().split())
len(s)
print(s)
import sys
m = re.match("商品名：(\w+), 価格：(\d+)円", "商品名：コーヒー, 価格：100円")
m.group()
m.group(0)
m.group(1)
s.map(lambda x: re.match(".*git clone\s(.*)\.git.*", x))
s
s2=s.map(lambda x: re.match(".*git clone\s(.*)\.git.*", x))
s2
s
s2
s2[2]
print(s2[2])
print(s2[5])
print(s2[100])
print(s2[101])
print(s2)
pd.set_option('display.max_rows', None)
print(s2)
s2=s.map(lambda x: re.match(".*git clone\s(.*)\.git.*", x).group(1))
s2=s.map(lambda x: re.match(".*git clone\s(.*)\.git.*", x).group())
m = re.match("商品名：(\w+), 価格：(\d+)円", "商品名：コーヒー, 価格：100円")
re.match("商品名：(\w+), 価格：(\d+)円", "商品名：コーヒー, 価格：100円").group(1)
s2=s.map(lambda x: re.match(".*git clone(.*).*", x).group())
s2=s.map(lambda x: re.match(".*git clone(.*).*", x).group(1))
s2=s.map(lambda x: (m = re.match(".*git clone(.*).*", x); m.group(1) if m else ""    )
s2=s.map(lambda x: (m = re.match(".*git clone(.*).*", x) m.group(1) if m else ""    )
s2=s.map(lambda x: re.match(".*git clone(.*).*", x))
print(s2)
s = pd.Series(sys.stdin.read().split())
s = pd.Series(sys.stdin.read().split("\n"))
print(s)
s2=s.map(lambda x: re.match(".*git clone(.*).*", x))
print(s2)
s2=s.map(lambda x: re.match(".*git clone(.*).*", x).group(1) if re.match(".*git clone(.*).*", x) else "")
s2=s.map(lambda x: re.match(".*git clone(.*)\.git.*", x).group(1) if re.match(".*git clone(.*).*", x) else "")
print(s2)
s2=s.map(lambda x: m.group(1) if m=re.match(".*git clone(.*).*", x) else "")
s2=s.map(lambda x: m=re.match(".*git clone(.*)\.git.*", x).group(1) if m else "")
s2=s.map(lambda x: re.match(".*git clone(.*)\.git.*", x) lambda y: y.group(1) if y else "")
s2=s.map(lambda x: re.match(".*git clone(.*)\.git.*", x) ,lambda y: y.group(1) if y else "")
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone(.*)\.git.*", x))
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone(.*)\.git.*", x)))
print(s2)
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone\shttps:(.*)\.git.*", x)))
print(s2)
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x)))
print(s2)
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).filter(lambda x: x)
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).filter(lambda x: if x != "")
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).filter(lambda x: x != "")
s[s != ""]
s2[s2 != ""]
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).filter(lambda x: x 
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).where(lambda x: x != "")
s2
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x))).filter(lambda x: x != "")
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x)))
s2
s2=s.map(lambda x: (lambda y: y.group(1) if y else "")(re.match(".*git clone https:(.*)\.git.*", x)))
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x)))
s2
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).str.contains('moji', na = False)]
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).str.contains(na = False)]
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).str.contains(na = False)
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).str.contains("",na = False)
s2
s2=s.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).dropna()
s2
series = pd.Series(np.arange(10))
import numpy as np
series = pd.Series(np.arange(10))
series.to_csv(sys.stdout)
series.to_csv(s2)
series.to_string(s2)
s2
print(s2)
s2.to_csv(".test.txt")
s2.to_csv("test.txt")
s2[1].to_csv("test.txt")
s2.to_csv("test.txt", index_col=0)
s2.to_csv("test1.txt", index=False)
quit
quit()
s2
import sys
import re
bf = pd.Series(sys.stdin.read().split("\n"))
import pandas as pd
bf = pd.Series(sys.stdin.read().split("\n"))
af=bf.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).dropna()
bf = pd.Series(sys.stdin.read().split("\n"))
af=bf.map(lambda x: (lambda y: y.group(1) if y else None)(re.match(".*git clone https:(.*)\.git.*", x))).dropna()
af
af.to_csv("test1.txt", index=False)
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x))
af
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x)).map(lambda x: x.group(1) if x else None)
af
pd.set_option('display.max_rows', None)
af
bf = pd.Series(sys.stdin.read().split("\n"))
bf
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x))
af
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x)).map(lambda x: x.group(1) if x else None)
af
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x)).map(lambda x: x.group(1) if x else None).dropna()
af
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x)).map(lambda x: x.group(1) if x else None).dropna()
af.to_csv("test2.txt", index=False)
bf = pd.Series(sys.stdin.read().split("\n"))
pd.set_option('display.max_rows', None)
print(bf)
af=bf.map(lambda x: re.match(".*git clone https:(.*)\.git.*", x)).map(lambda x: x.group(1) if x else None).dropna()
af.to_csv("test2.txt", index=False)
quit()
import pandas as pd
import sys
import re
bf = pd.Series(sys.stdin.read().split("\n"))
bf
pd.set_option('display.max_rows', 2)
bf
pd.set_option('display.max_rows', 100)
bf
print(bf)
pd.options.display.colheader_justify = 'left'
print(bf)
df.style.set_properties(**{'text-align': 'left'})
print(bf)
print(bf[0])
print(bf[1])
af = bf.map(lambda x: re.match("  (.*) (.*) (\s|,).*", x))
af
af = bf.map(lambda x: re.match("  (.*) (.*)[\s,].*", x))
af
af = bf.map(lambda x: re.match("  (.*) (.*)[\s,].*", x)).map(lambda y: f'カラム名は{y.group(1)}で、型は{y.group(2)}' if y else None)
af
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: f'カラム名は{y.group(1)}で、型は{y.group(2)}' if y else None)
af
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: f'カラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None)
af
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: f'テーブル名はstudy_qa1で\nカラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None)
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: f'テーブル名はs\
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None)
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None)
af
af.to_csv("testD1.txt", index=False)
af.to_csv("testD1.txt", index=False, quoting=csv.QUOTE_NONNUMERIC)
af.to_csv("testD1.txt", index=False, quoting=none)
af.to_csv("testD1.txt", index=False, quoting=None)
af.to_csv("testD1.txt", index=False, quoting=3)
af.to_csv("testD1.txt", index=False, quoting=2)
af.to_csv("testD1.txt", index=False, quoting=3)
af.dropna()
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
カラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None).dropna()
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。' if y else None).dropna()
af
af.to_csv("testD1.txt", index=False, quoting=3)
af.to_csv("testD1.txt", index=False)
af.to_clipboard()
af.tolist()
af.to_string()
af = af.tolist()
af
with open('olist.txt', 'w', encoding='utf-8', newline='\n') as f:
	f.writelines(af)
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。\n' if y else None).dropna()
with open('olist.txt', 'w', encoding='utf-8', newline='\n') as f:
	f.writelines(af)
with open('olist.txt', 'w', encoding='utf-8') as f:
	f.writelines(af)
with open('olist.txt', 'w', encoding='utf-8', newline='\n') as f:
	f.writelines(af)
with open('olist.txt', 'w') as f:
	f.writelines(af)
quit()
import pandas as pd
import sys
import re
bf = pd.Series(sys.stdin.read().split("\n"))
af = bf.map(lambda x: CREATE TABLE IF NOT EXISTS study_qa1
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  is_positive boolean not null DEFAULT TRUE,
  exp_val text,
  obj_val text,
  ins_date timestamp with time zone not null,
  update_date timestamp with time zone not null,
  del_flag boolean not null DEFAULT FALSE
quit()
import sys
import re
import pandas as pd
pd.set_option('display.max_row', 100)
bf = pd.Series(sys.stdin.read().split("\n"))
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*"))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。\n' if y else None).dropna().tolist()
af = bf.map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x))\
.map(lambda y: f'テーブル名は、study_qa1で、\n\
カラム名は{y.group(1)}で、型は{y.group(2)}です。\n' if y else None).dropna().tolist()
af
with open('ot2.txt', 'w', encoding='utf-8', newline="\n"):
with open('ot2.txt', 'w', encoding='utf-8', newline="\n") as f:
	f.writelines(af)
.quit()
quit()
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def to_list(self):
        return list(self.iterator)
i([2,1,15,-4,-5,-12]).map(lambda x: x*2).filter(lambda x: x <= 10).to_list()
from functools import reduce
reduce(lambda a: l.append(f'test: {a}'), ["aiu", "te2", "te3"], [])
reduce(lambda a: l.append(f'test: {a}'), ["aiu", "te2", "te3"])
reduce(lambda a: l.append(a), ["aiu", "te2", "te3"], [])
reduce(lambda a: [].append(f'test: {a}'), ["aiu", "te2", "te3"])
reduce(lambda a: l.append(f'test: {a}'), ["aiu", "te2", "te3"], [])
a_l = ["a", "b", "c" ]
a_l + ["d"]
a_l + "e"
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            acc.append(func(acc, cur, i, arr))
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
import sys
import re
bf = sys.stdin.read().split("\n")
bf
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).reduce(reduce_call_back)
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].toLowerCase()}) {')
    acc.append(f'			this.${arr[i].toLowerCase()}.add({arr[i].toLowerCase()});')
    acc.append(`		}`)
    return acc;  
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append(`		}`)
    return acc;  
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append(`		}}`)
    return acc; 
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}}')
    return acc; 
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            acc.append(func(acc, cur, i, li))
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).reduce(reduce_call_back)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None)
af
af.to_list()
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None)
af.to_list()
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
def reduce_call_back(acc, cur, i, arr):
    print(f'確認: {i}')
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}}')
    return acc;  
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            print(f'r確認: {i}')
            acc.append(func(acc, cur, i, li))
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            print(f'r確認: {i}')
            acc.append(func(acc, cur, i, li))
        return acc
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
def reduce_call_back(acc, cur, i, arr):
    print(f'確認: {i}')
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}')
    return acc;
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None)
af
af.to_list()
af.to_list()[0]
af.to_list()
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
af[1]
af[2]
af[3]
af[4]
af[3]
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            print(f'r確認: {i}')
            func(acc, cur, i, li)
        return acc
    def to_list(self):
        return list(self.iterator)
def reduce_call_back(acc, cur, i, arr):
    print(f'確認: {i}')
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}')
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
len(af)
af[0]
af[1]
af[2]
af[3]
af[4]
af[5]
af[6]
af[7]
af[8]
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, i, li)
        return acc
    def to_list(self):
        return list(self.iterator)
# コールバック関数
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}')
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, i, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'		public void add{arr[i]}(String {arr[i].lower()}) {{')
    acc.append(f'			this.${arr[i].lower()}.add({arr[i].lower()});')
    acc.append('		}')
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, i, li)
        return iter(acc)
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
af.to_list()
list(af)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None)
af
type(af)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, i, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for i, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, i, li)
        return i(acc)
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
af.to_list()
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).af.to_list()
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list()
af
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(list(self.iterator))
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(list(self.iterator))
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af
af.to_list()
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = self.iterator
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af
af.to_list()
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        copy_iterator = self.iterator
        return list(copy_iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af
af.to_list()
af
af.to_list()
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        return list(self.iterator)
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list()
af
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af
af.to_list()
af
list(af)
import itertools
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self.output_list
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        # return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
        
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af.join("\n")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self.output_list
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.to_list())
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back)
af.join("\n").to_save("mt1.txt")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self.output_list
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        # return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.output_str)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_save("mt1.txt")
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mt1.txt")
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        # return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.output_str)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mt1.txt")
import itertools
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.output_str)
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mt1.txt")
af
print(af)
class i(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return i(map(func, self.iterator))
    def filter(self, func):
        return i(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return i(iter(acc))
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.output_list = list(it2)
        return self
    def join(self, sep): # sep: "\n"等
        self.output_str = sep.join(self.output_list)
        return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.output_str)
        return self
af = i(bf).map(lambda x: re.match("  (.*?) (.*?)[\s,].*", x)).map(lambda y: y.group(1) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mt1.txt")
af
print(af)
af.output_list
af.output_str
af.to_list()
quit
quit()
import sys
import re
from mylib.mc import op_list
af = op_list.ListMc(read_str.split("\n")).map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)).map(lambda y: (y.group(1), y.group(2)) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mc1.txt")
af = op_list.ListMc(bf).map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)).map(lambda y: (y.group(1), y.group(2)) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mc1.txt")
bf = sys.stdin.read().split("\n")
af = op_list.ListMc(bf).map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)).map(lambda y: (y.group(1), y.group(2)) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mc1.txt")
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー')
    acc.append(f'カラム名は、{arr[i][0].lower()}です。')
    acc.append(f'型は、{arr[i][1].upper()}です。')
af = op_list.ListMc(bf).map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)).map(lambda y: (y.group(1), y.group(2)) if y else None).filter(lambda x: x != None).reduce(reduce_call_back).to_list().join("\n").to_save("mc1.txt")
af
from mylib.mc.op_list import ListMc
from mylib.mc.op_list import ListdMc
from mylib.mc.op_list import ListMc
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(reduce_call_back) \
    .to_list().join("\n") \
    .to_save("mc1.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(reduce_call_back) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
quit()
from mylib.mc.op_list import ListMc
quit()
from mylib.mc.op_list import ListMc
import sys
import re
bf = sys.stdin.read().split("\n")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(reduce_call_back) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr: \
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'カラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
    	]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr: \
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'xxxカラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
    	]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'xxxカラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
    	]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) 
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'xxxカラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
    	]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'xxxカラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
    	]
    ) \
    .to_list().join("\n") \
    .to_save("mc1.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'xxxカラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc1.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー'),
    	   acc.append(f'カラム名は、{arr[i][0].lower()}です。'),
    	   acc.append(f'型は、{arr[i][1].upper()}です。'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc1.txt")
quit()
import sys
import re
from mylib.mc.op_list import ListMc
j_type = {
    "INTEGER": "int",
    "REAL": "float",
    "text": "String",
    "BOOLEAN": "boolean",
    "timestamp": "Date",
}
j_type
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {j_type[arr[i][1]]} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0]}({j_type[arr[i][1]]} {arr[i][0]}) {{'),
           acc.append('}'),
           acc.append(f'public {j_type[arr[i][1]]} get{arr[i][0]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc1.txt")
bf = sys.stdin.read().split("\n")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {j_type[arr[i][1]]} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0]}({j_type[arr[i][1]]} {arr[i][0]}) {{'),
           acc.append('}'),
           acc.append(f'public {j_type[arr[i][1]]} get{arr[i][0]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {j_type.get([arr[i][1], "XXX")} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0]}({j_type.get([arr[i][1], "XXX")} {arr[i][0]}) {{'),
           acc.append('}'),
           acc.append(f'public {j_type.get([arr[i][1], "XXX")} get{arr[i][0]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {j_type.get(arr[i][1], "XXX")} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0]}({j_type.get(arr[i][1], "XXX")} {arr[i][0]}) {{'),
           acc.append('}'),
           acc.append(f'public {j_type.get(arr[i][1], "XXX")} get{arr[i][0]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {j_type.get(arr[i][1], "XXX")} {arr[i][0].lower()};'),
           acc.append(f'public set{arr[i][0][0].upper() + arr[i][0][1:]}({j_type.get(arr[i][1], "XXX")} {arr[i][0].lower()}) {{'),
           acc.append(f'    this.{arr[i][0].lower()} = {arr[i][0].lower()};'),
           acc.append('}'),
           acc.append(f'public {j_type.get(arr[i][1], "XXX")} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0].lower()};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: [ vns = x[0].split("_"), return (vns[0] + [1].capitalize(), j_type.get(x[1])])
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: [ vns := x[0].split("_"), return (vns[0] + [1].capitalize(), j_type.get(x[1])])
def cnvCamelCase(vName):
    sns = vname.split("_"):
    c_name = ""
    c_name += sns[0]
    for name in sns[1:]:
        c_name += name
def cnvCamelCase(vName):
    sns = vname.split("_")
    c_name = ""
    c_name += sns[0]
    for name in sns[1:]:
        c_name += name
    return c_name
def cnvCamelCase(vName):
    sns = vname.split("_")
    c_name = ""
    c_name += sns[0]
    for name in sns[1:]:
        c_name += name.capitalize()
    return c_name
cnvCamelCase(test_name_ades)
cnvCamelCase("test_name_ades")
def cnv_camel_case(v_name):
    sns = v_name.split("_")
    c_name = ""
    c_name += sns[0]
    for name in sns[1:]:
        c_name += name.capitalize()
    return c_name
cnv_camel_case("test_name_des1")
cnv_camel_case("test")
def cnv_camel_case(v_name):
    sns = v_name.split("_")
    c_name = sns[0]
    for name in sns[1:]:
        c_name += name.capitalize()
    return c_name
cnv_camel_case("test")
cnv_camel_case("test_name_des1")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1])))
af
af.to_list()
af.output_list
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX")))
af.to_list().output_list
def cnv_camel_case(v_name):
    sns = v_name.lower().split("_")
    c_name = sns[0]
    for name in sns[1:]:
        c_name += name.capitalize()
    return c_name
cnv_camel_case("test_deSesK_miHo")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX")))
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0].lower()};'),
           acc.append(f'public set{arr[i][0][0].upper() + arr[i][0][1:]}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX"))) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0].lower()};'),
           acc.append(f'public set{arr[i][0][0].upper() + arr[i][0][1:]}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX"))) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0].lower()};'),
           acc.append(f'public set{arr[i][0].capitalize()}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize())
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).to_list().output_list
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).output_list
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).reduce(lambda acc, cur, i, arr: acc + cur)
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).reduce(lambda acc, cur, i, arr: acc.append(cur))
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).reduce(lambda acc, cur, i, arr: acc.append(cur)).to_list().output_list
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).join("")
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).join("").to_list().output_list
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).join("").output_str
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).join("\n").output_str
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).to_list().join("\n").output_str
ListMc("test_des_des".split("_")).map(lambda s: s.capitalize()).to_list().join("").output_str
def cnv_camel_case(v_name):
    sns = v_name.lower().split("_")
    c_name = sns[0]
    for name in sns[1:]:
        c_name += name.capitalize()
    return c_name
def cnv_camel_case(v_name):
    return ListMc(v_name.lower().split("_")).map(lambda s: s.capitalize()) \
           .to_list().join("").output_str
cnv_camel_case("test_aiua_kak_de")
cnv_camel_case("test")
cnv_camel_case("Test")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX"))) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0].lower()};'),
           acc.append(f'public set{arr[i][0].capitalize()}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX"))) \
    .reduce(lambda acc, cur, i, arr:
        [
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0]}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("mc2.txt")
.save t.txt
help()
save
save()
help()
save
help(save)
%save
import readline
readline.write_history_file('history.py')
