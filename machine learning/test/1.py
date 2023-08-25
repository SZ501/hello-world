import json
import random
import numpy as np
from itertools import permutations
from itertools import combinations
print(len([[1,2],[3,4]]))
import numpy as np
import openpyxl
import json
import random
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
'''
#okfine66
wb=openpyxl.load_workbook('C:\\Users\\47257\\Desktop\\influence_data.xlsx')
sheet=wb['influence_data']
a0=list(sheet.columns)[0]
a1=list(sheet.columns)[4]
b0=list(sheet.columns)[2]
b1=list(sheet.columns)[6]
K={}
for i in (range(len(a0))):
    K[a0[i].value]=b0[i].value
for i in range(len(a0)):
    K[a1[i].value]=b1[i].value
del K["influencer_id"]
del K["follower_id"]
with open('C:\\Users\\47257\\Desktop\\4.json','w')as f1:
    json.dump(K,f1)
'''

wb=openpyxl.load_workbook("C:\\Users\\47257\\Desktop\\12.xlsx")
print(type(wb))
print('begin')
sheet=wb['data_by_artist']
tup=list(sheet.columns)[1]
with open("C:\\Users\\47257\\Desktop\\6.json",'r')as f1:
    a0=json.load(f1)
j=2
for i in tup[1:]:
    if str(i.value) in a0.keys():
        sheet[f'Q{j}']=a0[str(i.value)]
    j=j+1
wb.save('C:\\Users\\47257\\Desktop\\12.xlsx')
