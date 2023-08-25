import openpyxl
import numpy as np
import json
import random
import time
import matplotlib.pyplot as plt
import copy
from collections import Counter
from itertools import combinations
wb=openpyxl.load_workbook("C:\\Users\\47257\\Desktop\\data\\题目五\\23.xlsx")
sheet=wb['Sheet1']
tlt=['A','B','C','D','E','F','G','H','I','J','K']
A=['danceability',	'energy',	'valence',	'tempo','loudness',	'acousticness',	'instrumentalness',	'liveness',	'speechiness',	'duration_ms']
'''
def solve_0(j,sheet,sheet1,qe):
    i=1  #i是年份有多少个
    while(True):
        k_0=j+i
        if(sheet[f'M{j}'].value==sheet[f'M{k_0}'].value):
            i=i+1
        else:
            break
    ty=[]
    for e in tlt:
        temp_0=0
        for t in range(i):
            k_1=j+t
            temp_0=float(sheet[f'{e}{k_1}'].value)+temp_0
        ty.append(temp_0)
    ty=[x/i for x in ty]
    ju=0
    for t in tlt:
        sheet1[f'{t}{qe}']=ty[ju]
        sheet1[f'M{qe}']=sheet[f'M{j}'].value
        ju=ju+1
    j=j+i
    return j
qe=2
j=2
while(j<46270):
    j=solve_0(j,sheet,sheet1,qe)
    qe=qe+1
wb1.save("C:\\Users\\47257\\Desktop\\data\\题目五\\22.xlsx")
'''

all={}
def solve_5(sheet,all,row):
    for i in range(1,row+1,1):
        if i==1:
            year=str(sheet[f'K{i}'].value)
            all[year]={}
            templist=[]
            for j in tlt[0:-1]:
                templist.append(sheet[f'{j}{i}'].value)
            all[year]['clist']=list(combinations(templist, 3))
            all[year]['strlist']=list(combinations(A, 3))
        else:
            year=str(sheet[f'K{i}'].value)
            all[year]={}
            templist=[]
            for j in tlt[0:-1]:
                templist.append(sheet[f'{j}{i}'].value)
            nowcombin=list(combinations(templist, 3))
            all[year]['clist']=nowcombin
            all[year]['strlist']=list(combinations(A, 3))
            lastcombin=all[lastyear]['clist']
            temps=[]
            for k in range(len(nowcombin)):
                t1=np.array([nowcombin[k]])
                t2=np.array([lastcombin[k]])
                s=np.dot(t1,t2.T)/np.sqrt(np.dot(t1,t1.T)*np.dot(t2,t2.T))
                temps.append(float(s))
            all[year]['slist']=temps
            smin=min(temps)
            idx=temps.index(smin)
            strt=all[year]['strlist'][idx]
            vsc=all[year]['clist'][idx]
            all[year]['smin']=smin
            all[year]['strt']=strt
            all[year]['vsc']=vsc
        lastyear=year


solve_5(sheet,all,19)
with open('C:\\Users\\47257\\Desktop\\data\\题目五\\1.json','w')as f1:
    json.dump(all,f1)
allto={}
for i,j in all.items():
    if i =='1925':
        continue
    allto[i]={}
    smin=all[i]["smin"]
    vsc=all[i]['vsc']
    strt=j['strt']
    allto[i]['smin']=smin
    allto[i]['strt']=strt
    allto[i]['vsc']=vsc
with open('C:\\Users\\47257\\Desktop\\data\\题目五\\2.json','w')as f1:
    json.dump(allto,f1)