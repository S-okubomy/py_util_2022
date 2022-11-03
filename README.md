## Pythonインタプリタでメソッドチェーン使いたいので、便利クラス作成

### 使い方
```
# 「mylib」ディレクトリと同じ階層で、Pythonインタプリタを起動
$ python3

# 作ったUtilを読み込み
>>> from mylib.mc.op_list import ListMc
>>> import sys
>>> import re

# （例）標準入力で以下の文字列読み取り
>>> bf = sys.stdin.read().split("\n")
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  is_positive boolean not null DEFAULT TRUE,
  exp_val text,
  obj_val text,
  ins_date timestamp with time zone not null,
  update_date timestamp with time zone not null,
  del_flag boolean not null DEFAULT FALSE

# 上記のお試し文字列コピペしたら「ctrl」+「D」を押して標準入力終了する

# 以下のコードを貼り付けます。
# (「mc1.txt」と言うファイルが作成されます)
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
```

### 例1
```
# 以下は使い方の例
# テーブルのカラム名と型からJavaのsetterとgetter作り

# 「mylib」ディレクトリと同じ階層で、Pythonインタプリタを起動
$ python3

# 作ったUtilを読み込み
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

def cnv_camel_case(v_name):
    return ListMc(v_name.lower().split("_")) \
        .reduce(lambda acc, cur, i, arr: acc.append(cur.capitalize()) if i !=0 else acc.append(cur)) \
        .to_list().join("").val

# （例）標準入力で以下の文字列読み取り
bf = sys.stdin.read().split("\n")
# サンプルの標準入力用
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  is_positive boolean not null DEFAULT TRUE,
  col_val REAL,
  obj_val text,
  ins_date timestamp with time zone not null,
  del_flag BOOLEAN not null DEFAULT FALSE

# 上記のお試し文字列コピペしたら「ctrl」+「D」を押して標準入力終了する

# 以下のコードを貼り付けます。
# (「exam1.txt」と言うファイルが作成されます)
af = ListMc(bf) \
    .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
    .map(lambda y: (y.group(1), y.group(2)) if y else None) \
    .filter(lambda x: x != None) \
    .map(lambda x: (cnv_camel_case(x[0]), j_type.get(x[1], "XXX"))) \
    .reduce(lambda acc, cur, i, arr:
        [           
           acc.append(f'ーーー {i+1}行目のテーブル定義より ーーー'),
           acc.append(f'private {arr[i][1]} {arr[i][0]};'),
           acc.append(f'public set{arr[i][0].capitalize()}({arr[i][1]} {arr[i][0]}) {{'),
           acc.append(f'    this.{arr[i][0]} = {arr[i][0]};'),
           acc.append('}'),
           acc.append(f'public {arr[i][1]} get{arr[i][0][0].upper() + arr[i][0][1:]}() {{'),
           acc.append(f'    return {arr[i][0]};'),
           acc.append('}'),
        ]
    ) \
    .to_list().join("\n") \
    .to_save("exam1.txt")

```

### 例２
```
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h
# https://atcoder.jp/contests/math-and-algorithm/submissions/36173535
>>> n, s = map(int, input().split())
869 120
>>> ListMc([r_num + b_num for r_num in range(1,n+1) for b_num in range(1,n+1)]).filter(lambda x: x <= s).reduce(lambda acc, cur: acc + 1, 0).val
7140

>>> a = ListMc(range(1,n+1)).map(lambda i: ListMc(range(1,n+1)).map(lambda j: j+i).to_list().list).flatten().filter(lambda x: x <= s).to_list().count()
>>> a.val
7140
```


### other 
```
# Pythonのインタラクティブシェルで打ったコマンドをファイルに保存
import readline
readline.write_history_file('history1.py')

# モジュールの再読込
import importlib
import mylib
importlib.reload(mylib.mc.op_list)
from mylib.mc.op_list import ListMc
```

### …or create a new repository on the command line
echo "# test_rust_2021" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/S-okubomy/test_rust_2021.git  
git push -u origin main  

### …or push an existing repository from the command line
git remote add origin https://github.com/S-okubomy/test_rust_2021.git  
git branch -M main  
git push -u origin main  

### …or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.  