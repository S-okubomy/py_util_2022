import itertools
import inspect
import functools
import operator

class li(object):
    def __init__(self, input_arg1 = None):
        if input_arg1 is None:
            self.val = ""
            return
        
        if isinstance(input_arg1, str): # 引数がStringだったら、valセットして終わり
            self.val = input_arg1
            return

        if hasattr(input_arg1, '__iter__'):  # 引数がiterableかどうか
            it1, it2 = itertools.tee(input_arg1, 2)
            self.iterator = it1
            self.list = list(it2)
            return
        
        raise TypeError("The constructor argument type is invalid.")
    def map(self, func):
        return li(map(func, self.iterator))
    def filter(self, func):
        return li(filter(func, self.iterator))
    def reduce(self, func, default_init_val = None):
        def get_func_res(args_len, func, acc, cur, index):
            if args_len == 2:
                acc = func(acc, cur)
            elif args_len == 3:
                acc = func(acc, cur, index)
            elif args_len == 4:
                acc = func(acc, cur, index, li)
            else:
                raise TypeError("Incorrect number of arguments")
            return acc
        li = list(self.iterator)
        if default_init_val is None:
            default_init_val = []
        acc = default_init_val
        args_len = len(inspect.getfullargspec(func).args)
        if isinstance(acc, list):
            for index, cur in enumerate(li):
                # リストの場合、accは参照渡しでfunc内でappendされる前提なので、リターンされるaccは未使用。
                get_func_res(args_len, func, acc, cur, index)
            self.iterator = iter(acc)
            self.list = acc
        else:
            for index, cur in enumerate(li):
                acc = get_func_res(args_len, func, acc, cur, index)
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
    def split(self, sep): # sep: "\n"等
        li = self.val.split(sep)
        self.iterator = iter(li)
        self.list = li
        return self
    def save(self, file_path):
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(self.val)
        return self
    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.val = f.read().rstrip()
        return self


###################################################################################################
# 以下は単体テスト用
# コマンド: python3 -m unittest mylib/mc/op_list.py 
import unittest
import os
import re

File_PATH_SEP = os.sep  # OSのセパレータ設定
TEST_FILE_RELATIVE_PATH = "test"

class TestOpList(unittest.TestCase):

    def test1_map(self):
        act = li([0,1,2,3]).map(lambda x: 2 * x).list
        self.assertEqual(act, [0,2,4,6])
    
    def test2_filter(self):
        act = li([0,1,2,3,4,5]).filter(lambda x: x > 2).list
        self.assertEqual(act, [3,4,5])
    
    def test3_reduce_for_list(self):
        act1 = li([0,1,2,3]).reduce(lambda acc, cur: acc.append([cur, 2 * cur])).list
        self.assertEqual(act1, [[0,0], [1,2], [2,4], [3,6]])

        act2 = li([0,1,2,3]).reduce(lambda acc, cur, i: acc.append([i + 1, 2 * cur])).list
        self.assertEqual(act2, [[1,0], [2,2], [3,4], [4,6]])

        act3 = li([0,1,2,3]).reduce(lambda acc, cur, i, arr: acc.append([i + 1, cur + arr[2]])).list
        self.assertEqual(act3, [[1, 2], [2,3], [3,4], [4,5]])

        # 例外のメッセージも含めてテスト(引数の数が不正な場合、エラーとなること)
        with self.assertRaises(TypeError) as cm:
            li([0,1,2,3]).reduce(lambda : "error test")
        self.assertEqual(cm.exception.args[0], 'Incorrect number of arguments')

        with self.assertRaises(TypeError) as cm:
            li([0,1,2,3]).reduce(lambda acc, cur, i, arr, err_arg: acc.append([i + 1, cur + arr[2]])).list
        self.assertEqual(cm.exception.args[0], 'Incorrect number of arguments')

    def test4_reduce_for_val(self):
        act1 = li([0,1,2,3,4,5]).reduce(lambda acc, cur: acc + cur, 0).val
        self.assertEqual(act1, 15)

        act2 = li([0,1,2,3,4,5]).reduce(lambda acc, cur, i: acc + cur + i, 0).val
        self.assertEqual(act2, 30)

        act3 = li([0,1,2,3,4,5]).reduce(lambda acc, cur, i, arr: acc + cur + i + arr[3], 0).val
        self.assertEqual(act3, 48)

        # 例外のメッセージも含めてテスト(引数の数が不正な場合、エラーとなること)
        with self.assertRaises(TypeError) as cm:
            li([0,1,2,3]).reduce(lambda : "error test", 0)
        self.assertEqual(cm.exception.args[0], "Incorrect number of arguments")

        with self.assertRaises(TypeError) as cm:
            li([0,1,2,3]).reduce(lambda acc, cur, i, arr, err_arg: "error test", 0)
        self.assertEqual(cm.exception.args[0], "Incorrect number of arguments")

    def test5_flatten(self):
        act1 = li([[0,1,2], [3,4,5,6,7], [8,9,10]]).flatten().list
        self.assertEqual(act1, [0,1,2,3,4,5,6,7,8,9,10])

    def test6_any(self):
        act1 = li([0,1,2,3,4,5]).any(lambda x: x >= 3)
        self.assertTrue(act1)

        act2 = li([0,1,2,3,4,5]).any(lambda x: x > 10)
        self.assertFalse(act2)

        act3 = li([0,1,2,3,4,5]).any(lambda x: x >= 0)
        self.assertTrue(act3)

        act4 = li([0,1,2,3,4,5]).any(lambda x: x >= 5)
        self.assertTrue(act4)

        act5 = li([0,1,2,3,4,5]).any(lambda x: x >= 6)
        self.assertFalse(act5)

        act6 = li([0,1,2,3,4,5]).any(lambda x: x < 0)
        self.assertFalse(act6)

    def test7_count(self):
        act = li([1,2,3,4,5]).count().val
        self.assertEqual(act, 5)

        act = li([]).count().val
        self.assertEqual(act, 0)

    def test8_join(self):
        act = li(["a","b","c", "d", "e"]).join("").val
        self.assertEqual(act, "abcde")

        act = li([0,1,2,3,4,5]).map(lambda x: str(x)).join("").val
        self.assertEqual(act, "012345")

        act = li(["a","b","c", "d", "e"]).join("-").val
        self.assertEqual(act, "a-b-c-d-e")

        act = li([]).join("-").val
        self.assertEqual(act, "")

    def test9_split(self):
        act = li("abc,def,ghi").split(",").map(lambda s: f'input: {s}').list
        self.assertEqual(act, ["input: abc", "input: def", "input: ghi"])

        act = li("abc\ndef\nghi").split("\n").map(lambda s: f'input: {s}').list
        self.assertEqual(act, ["input: abc", "input: def", "input: ghi"])

        act = li("").split("\n").list
        self.assertEqual(act, [""])

    def test10_save_and_read(self):
        test_file_path1 = os.path.join(TEST_FILE_RELATIVE_PATH, "test10_act_save_out1.txt")
        li(["abc","def","ghi"]).join("\n").save(test_file_path1)
        act = li().read(test_file_path1).val
        self.assertEqual(act, "abc\ndef\nghi")

        test_file_path2 = os.path.join(TEST_FILE_RELATIVE_PATH, "test10_act_save_out2.txt")
        li("testabc\naiueo\nkakikukeko").save(test_file_path2)
        act = li().read(test_file_path2).val
        self.assertEqual(act, "testabc\naiueo\nkakikukeko")

    def test11_exam0(self):
        act_file_path1 = os.path.join(TEST_FILE_RELATIVE_PATH, "test11_act_exam0.txt")
        bf = """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_positive boolean not null DEFAULT TRUE,
            exp_val text,
            obj_val text,
            ins_date timestamp with time zone not null,
            update_date timestamp with time zone not null,
            del_flag boolean not null DEFAULT FALSE
        """
        # 上記データ(bf)を整形してファイル出力
        af = li(bf) \
            .split("\n") \
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
            .save(act_file_path1)
        
        # 上記出力結果が期待値と一致しているかの確認
        act = li().read(act_file_path1).val  # 実際に出力した結果
        expected_file_path1 = os.path.join(TEST_FILE_RELATIVE_PATH, "test11_excepted_exam0.txt")
        excepted = li().read(expected_file_path1).val  # 期待値の読み込み
        self.assertEqual(act, excepted)

    def test12_exam1(self):
        j_type = {
            "INTEGER": "int",
            "REAL": "float",
            "text": "String",
            "BOOLEAN": "boolean",
            "timestamp": "Date",
        }
        def cnv_camel_case(v_name):
            return li(v_name.lower().split("_")) \
                .reduce(lambda acc, cur, i, arr: acc.append(cur.capitalize()) if i !=0 else acc.append(cur)) \
                .to_list().join("").val

        act_file_path1 = os.path.join(TEST_FILE_RELATIVE_PATH, "test12_act_exam0.txt")
        bf = """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_positive boolean not null DEFAULT TRUE,
            col_val REAL,
            obj_val text,
            ins_date timestamp with time zone not null,
            del_flag BOOLEAN not null DEFAULT FALSE
        """
        # 上記データ(bf)を整形してファイル出力
        af = li(bf) \
            .split("\n") \
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
            .save(act_file_path1)
        
        # 上記出力結果が期待値と一致しているかの確認
        act = li().read(act_file_path1).val  # 実際に出力した結果
        expected_file_path1 = os.path.join(TEST_FILE_RELATIVE_PATH, "test12_excepted_exam0.txt")
        excepted = li().read(expected_file_path1).val  # 期待値の読み込み
        self.assertEqual(act, excepted)

    def test13_exam2(self):
        # https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h
        # https://atcoder.jp/contests/math-and-algorithm/submissions/36173535
        n, s = (869, 120)
        act1 = li([r_num + b_num for r_num in range(1,n+1) for b_num in range(1,n+1)]).filter(lambda x: x <= s).reduce(lambda acc, cur: acc + 1, 0).val
        self.assertEqual(act1, 7140)

        act2 = li(range(1,n+1)).map(lambda i: li(range(1,n+1)).map(lambda j: j+i).to_list().list).flatten().filter(lambda x: x <= s).to_list().count().val
        self.assertEqual(act2, 7140)

    def test14_exam3(self):
        #https://atcoder.jp/contests/math-and-algorithm/submissions/36250286
        n = 10
        import math
        act1 = li(range(2,n+1)).filter(lambda x: not li(range(2, int(math.sqrt(x)+1))).any(lambda i: x % i == 0)).map(lambda x: str(x)).to_list().join(" ").val
        self.assertEqual(act1, '2 3 5 7')


###################################################################################################
# 以下は使い型の例
# (例)reduceのコールバック関数
def reduce_call_back(acc, cur, i, arr):
    acc.append(f'ーーー {i+1}行目のテーブル定義 ーーー')
    acc.append(f'カラム名は、{arr[i][0].lower()}です。')
    acc.append(f'型は、{arr[i][1].upper()}です。')

if __name__ == '__main__':

    # unittest.main()   # unit test用

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
        .join("\n") \
        .save("mc1.txt")