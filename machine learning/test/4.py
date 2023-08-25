import openpyxl
import numpy as np
import json
import random
import time
import matplotlib.pyplot as plt
import copy
from itertools import combinations
wb=openpyxl.load_workbook('C:\\Users\\47257\\Desktop\\data\\work\\fim.xlsx')
art=wb['artist']
f1=wb['f1']
tlt=['C','D','E','F','G','H','I','J','K','L']
SS=wb['SS']
S1=wb['S1']
A=['danceability',	'energy',	'valence',	'loudness',	'acousticness',	'instrumentalness',	'liveness',	'speechiness',	'duration_ms',	'popularity']
B=[0.521975456	,0.546826974,	0.619659538	,0.484134812,	0.360355932	,0.051906132,	0.223001337,	0.53395018	,0.87153935	,0.961215067]
S=[0.5756,	0.772923077	,0.564112308	,0.330900769,	0.135681417	,0.139693162	,0.281252308	,0.43835385	,1.335057769,	0.999384615]
def solve4c(aim,sheet,num):
    strlist_0=list(combinations(A, 3))
    aimlist_0=list(combinations(aim, 3))
    aimlist_1=np.array(aimlist_0)
    tar=[]
    r1=np.array([[]])
    ru=0
    for i in range(2,num+1,1):
        r2=np.array([[]])
        templist=[]
        templist1=[]
        templist2=[0,0,0,0,0,0,0,0,0,0]
        for j in tlt:
            print(sheet[f'{j}{i}'].value)
            templist.append(sheet[f'{j}{i}'].value)
        mk=list(combinations(templist, 3))
        for k in range(len(mk)):
            t1=np.array([mk[k]])
            t2=aimlist_1[k]
            s=np.dot(t1,t2.T)/np.sqrt(np.dot(t1,t1.T)*np.dot(t2,t2.T))
            s=float(s)
            templist1.append(s)
        tp=0
        for u in A:
            for k in range(0,120,1):
                if u in strlist_0[k]:
                    templist2[tp]=templist2[tp]+templist1[k]
            tp=tp+1
        tar.append(copy.deepcopy(templist2))
        ru=ru+1
        print(ru)
    return tar



tar=solve4c(S,S1,165)
print(len(tar))
wb1=openpyxl.Workbook()
sheet=wb1.active
for i in range(len(tar)):
    tp=0
    for j in tlt:
        sheet[f'{j}{i+2}']=tar[i][tp]
        tp=tp+1
wb1.save('C:\\Users\\47257\\Desktop\\data\\4.xlsx')
    
print('end')