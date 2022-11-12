import itertools
import inspect
import functools
import operator

class li(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.list = []
        self.val = ""
    def map(self, func):
        return li(map(func, self.iterator))
    def filter(self, func):
        return li(filter(func, self.iterator))
    def reduce(self, func, default_init_val = None):
        li = list(self.iterator)
        if default_init_val is None:
            default_init_val = []
        acc = default_init_val
        args_len = len(inspect.getfullargspec(func).args)
        # print(f'確認数: {args_len}')
        if isinstance(acc, list):
            if args_len == 2:
                for index, cur in enumerate(li):
                    func(acc, cur)
            elif args_len == 3:
                for index, cur in enumerate(li):
                    func(acc, cur, index)
            elif args_len == 4:
                for index, cur in enumerate(li):
                    func(acc, cur, index, li)
            else:
                raise ValueError("Incorrect number of arguments")
            self.iterator = iter(acc)
            self.list = acc
        else:
            if args_len == 2:
                for index, cur in enumerate(li):
                    acc = func(acc, cur)
            elif args_len == 3:
                for index, cur in enumerate(li):
                    acc = func(acc, cur, index)
            elif args_len == 4:
                for index, cur in enumerate(li):
                    acc = func(acc, cur, index, li)
            else:
                raise ValueError("Incorrect number of arguments")
            self.val = acc
        return self
    def flatten(self):
        flat_list = functools.reduce(operator.add, list(self.iterator))
        self.iterator = iter(flat_list)
        self.list = flat_list
        return self
    def any(self, func):
        li = list(self.iterator)
        for item in li:
            if func(item):
                return True
        return False
    def count(self):
        self.val = len(self.list)
        return self
    def to_list(self):
        it1, it2 = itertools.tee(self.iterator, 2)
        self.iterator = it1
        self.list = list(it2)
        return self
    def join(self, sep): # sep: "\n"等
        self.val = sep.join(self.list)
        return self
    def to_save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.val)
        return self


###################################################################################################
# 以下は使い型の例
# (例)reduceのコールバック関数
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー')
    acc.append(f'カラム名は、{arr[i][0].lower()}です。')
    acc.append(f'型は、{arr[i][1].upper()}です。')

if __name__ == '__main__':
    import re

    # リスト関連の操作をメソッドチェーンで使う例
    read_str = """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        is_positive boolean not null DEFAULT TRUE,
        exp_val text,
        ins_date timestamp with time zone not null,
    """
    af = li(read_str.split("\n")) \
        .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
        .map(lambda y: (y.group(1), y.group(2)) if y else None) \
        .filter(lambda x: x != None) \
        .reduce(reduce_call_back) \
        .to_list().join("\n") \
        .to_save("mc1.txt")