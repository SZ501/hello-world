from collections import Counter
import numpy as np
import openpyxl
import json
import random
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
wb=openpyxl.load_workbook("C:\\Users\\47257\\Desktop\\data\\题目六\\r1.xlsx")
wb1=openpyxl.Workbook()
sheet1=wb1.active
sheet=wb['Sheet1']
tr=[]
def solve_0(j,sheet):
    i=1  #i是追随了多少人
    while(True):
        k_0=j+i
        if(sheet[f'Q{j}'].value==sheet[f'Q{k_0}'].value):
            i=i+1
        else:
            break
    temp_0=0
    R=[]
    for t in range(i):
        k_1=j+t
        R.append(sheet[f'S{k_1}'].value)
    T=Counter(R)
    most_counterNum = T.most_common(1)
    mst=most_counterNum[0][0]
    tr.append([sheet[f'Q{j}'].value,mst])
    j=j+i
    return j
j=2
while(j<46270):
    j=solve_0(j,sheet)
with open('C:\\Users\\47257\\Desktop\\data\\题目六\\2.json','w')as f1:
    json.dump(tr,f1)
ou=1
for k in tr:
    sheet1[f'A{ou}']=k[0]
    sheet1[f'B{ou}']=k[1]
    ou=ou+1
wb1.save('C:\\Users\\47257\\Desktop\\data\\题目六\\jl.xlsx')
