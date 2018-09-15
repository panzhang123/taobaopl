import numpy as np
import pandas as pd
import requests
import re
k=requests.get(url='https://rate.tmall.com/list_detail_rate.htm?itemId=40452825264&sellerId=1680285850&currentPage=2')
print(k.text)
g=re.compile('jsonp128\((.*)\)')
g1=g.findall(k.text)
print(g1)
p=pd.read_json(g1[0],orient="values",encoding='utf-8')
for i in range(len(p.T['rateList'][0])):
    print("用户名："+p.T['rateList'][0][i]['displayUserNick'])
    print("评价："+p.T['rateList'][0][i]['rateContent'])
    print("商家回复："+p.T['rateList'][0][i]['reply'])
    print()