import sys
import re
import mylib
from mylib.mc.op_list import li
import datetime
# import numpy as np  # バージョンによりエラー出るためコメントアウト
import random

class Man:
    def __init__(self, hp):
        self.hp = hp
    
    def up(self, val):
        self.hp += val

    def down(self, val):
        self.hp -= val

    def print_hp(self):
        print(f'Hp: {self.hp}')
    
    def is_happen(self, *rates):
        for r in rates:
            if random.random() > r:
                return False
        return True

class Pman1(Man):
    def do_sport(self, val):
        self.hp += 2 * val

    def do_study(self):
        super().down(5)


if __name__ == '__main__':
    m = Man(100)
    m.print_hp()
    m.down(10)
    m.print_hp()
    m.up(5)
    m.print_hp()
    print(m.is_happen(0.5))
    
    pm1 = Pman1(70)
    pm1.print_hp()
    pm1.do_sport(5)
    pm1.print_hp()
    pm1.do_study()
    pm1.print_hp()