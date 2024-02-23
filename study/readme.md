●実行方法
```
~/ws-2024-1/py_util_2022$ python -m study.sim1 
~/ws-2024-1/py_util_2022$ python study/per1.py 
```

●bpythonでの実行
```
>>> import sim1
>>> importlib.reload(sim1)
>>> from sim1 import Pman1
>>> pm1 = Pman1(77)
>>> pm1.print_hp()
Hp: 77
>>> pm1.up(3)
>>> pm1.print_hp()
Hp: 80
```