import itertools

class ListMc(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.output_list = []
        self.output_str = ""
    def map(self, func):
        return ListMc(map(func, self.iterator))
    def filter(self, func):
        return ListMc(filter(func, self.iterator))
    def reduce(self, func):
        li = list(self.iterator)
        acc = []
        for index, cur in enumerate(li):
            # accにコールバック関数で文字列追加
            func(acc, cur, index, li)
        return ListMc(iter(acc))
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
    af = ListMc(read_str.split("\n")) \
        .map(lambda x: re.match(".*?([a-zA-Z_]+) (.*?)[\s,].*", x)) \
        .map(lambda y: (y.group(1), y.group(2)) if y else None) \
        .filter(lambda x: x != None) \
        .reduce(reduce_call_back) \
        .to_list().join("\n") \
        .to_save("mc1.txt")

