## メモ

### python

●何日前
```
import datetime
now = datetime.datetime(2022,11,24)
priv_date = now - datetime.timedelta(days=60)
print(priv_date)
```

●次回開始日時
```
import datetime
import math
now = datetime.datetime(2023,6,16,9,0,0); start = datetime.datetime(2023,6,1,10,0,0); prio = datetime.timedelta(days=7);
d_rate = (now.timestamp() - start.timestamp()) / (prio.total_seconds())
rate = max(math.ceil(d_rate), 1)
next = start.timestamp() + prio.total_seconds() * rate
print(datetime.datetime.fromtimestamp(next))
```

●format
```
# 2進数0埋め
>>> f'{256:016b}'
'0000000100000000'
```

●複利
```
def disp_loan(zandaka, kinri, hensai, kikan=100):
    init_zan = zandaka; nen_hensai = hensai * 12; hg = nen_hensai;
    for y in range(kikan):
        zandaka += (zandaka * kinri/100) - nen_hensai;
        if zandaka <= 0:
            return
        print(f'{y+1}年目({38+y})才: zan={zandaka:,.0f}, hg={hg:,.0f} risoku={hg-init_zan:,}')
        hg += nen_hensai;

>>> disp_loan(34_900_000, 0.45, 89_826) 
```

### コマンド
●ファイル書き換え
```
OLD_VER='6\.12\.[0-9]\+\.[0-9]\+'
NEW_VER='7\.13\.0\.0'
sed -i -e "s/${OLD_VER}/${NEW_VER}/" path/dir/test.txt
```

●繰り返し
```
words=("aaa" "bbb" "ccc"); \
for w in ${words[@]}; do echo ${w}; echo "test bbb xxx" | grep ${w}; done
```

●検索
```
sudo grep -r --include='*.log*' "test.*str" /home/user/dir
```

●git
```
git rev-list --all | xargs git grep -e "dfs.*bef.*"
git show xxxxx:./atc0.rs
```

●os
```
du -h | grep -E "[0-9]+\.?[0-9]+G.*" | sort -nk 1
sudo du -sh *
sudo du -d 1 -h *
watch -n 0.1 -d ps  | grep java | grep -v grep
```

●解凍
```
find ./ -type f -name "*.gz" -exec gunzip {} \;
find ./ -type f -name "*.tar.gz" -exec tar -xzf {} \;
```

●正規表現
```
#カンマ、あってもなくても
li(["  , a1 xxx", "a2 xxx", "  a3 xxx"]).map(lambda s: re.match("\s{2},?\s?(.*?)\s.*", s)).map(lambda m: m.group(1) if m else None).filter(lambda s: s != None).list
```

### その他 参考文献
https://knooto.info/python-snippets/