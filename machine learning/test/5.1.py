import openpyxl
import numpy as np
import json
import random
import time
import matplotlib.pyplot as plt
import copy
from collections import Counter
from itertools import combinations
wb=openpyxl.load_workbook("C:\\Users\\47257\\Desktop\\data\\题目五\\1\\4.xlsx")
wb1=openpyxl.Workbook()
sheet1=wb1.active
sheet=wb['Sheet1']
tlt=['C','D','E']
A=['danceability',	'energy',	'valence',	'tempo','loudness',	'acousticness',	'instrumentalness',	'liveness',	'speechiness',	'duration_ms']
def solve_0(j,sheet,sheet1,qe,ki):
    i=1  #i是年份有多少个
    while(True):
        k_0=j+i
        if(sheet[f'B{j}'].value==sheet[f'B{k_0}'].value):
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
        sheet1[f'A{qe}']=sheet[f'A{j}'].value
        sheet1[f'B{qe}']=sheet[f'B{j}'].value
        ju=ju+1
    j=j+i
    return j
def main(num):
    qe=2
    j=2
    ki=[]
    while(j<num):
        j=solve_0(j,sheet,sheet1,qe,ki)
        qe=qe+1
    wb1.save("C:\\Users\\47257\\Desktop\\data\\题目五\\1\\4.1.xlsx")
num=3290
main(num)