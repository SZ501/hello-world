import openpyxl
import numpy as np
import json
import random
import time
import matplotlib.pyplot as plt
import copy
wb=openpyxl.load_workbook('C:\\Users\\47257\\Desktop\\data\\work\\fid.xlsx')
t1=wb['t1']
art=wb['artist']
f1=wb['f1']
tempi=wb['tempi']
o1=wb['o1']
target=wb['target']
tlt=['A','B','C','D','E','F','G','H','I','J','K','L']
templist=[]
SS=wb['SS']
S1=wb['S1']
for i in range(2,167,1):
    templist.append(SS[f'E{i}'].value)
print(len(templist))
tp_0=2
for i in templist:
    for j in range(2,5857,1):
        if(art[f'B{j}'].value==i):
            for k in tlt:
                S1[f'{k}{tp_0}']=art[f'{k}{j}'].value
            tp_0=tp_0+1
wb.save('C:\\Users\\47257\\Desktop\\data\\work\\fim.xlsx')

'''
tep=copy.deepcopy(templist)

p=0
for i in templist:
    p=p+1
    print(p)
    for j in range(2,42771,1):
        if(tempi[f'A{j}'].value==i):
            tep.append(tempi[f'E{j}'].value)
with open('C:\\Users\\47257\\Desktop\\data\\work\\1.json','w')as f1:
    json.dump(tep,f1)
'''
'''
tp_0=2
with open('C:\\Users\\47257\\Desktop\\data\\work\\1.json','r')as f1:
    templist=json.load(f1)
templist=set(templist)
templist=list(templist)
for j in range(2,5854,1):
    if (art[f'B{j}'].value not in templist):
        for k in tlt:
            o1[f'{k}{tp_0}']=art[f'{k}{j}'].value
        tp_0=tp_0+1
wb.save('C:\\Users\\47257\\Desktop\\data\\work\\fit.xlsx')
'''
'''
r=list(random.sample(list(range(2,3049,1)),600))
print(r)
tp_0=2
for i in r:
        for k in tlt:
            target[f'{k}{tp_0}']=o1[f'{k}{i}'].value
        tp_0=tp_0+1
wb.save('C:\\Users\\47257\\Desktop\\data\\work\\fid.xlsx')
'''

