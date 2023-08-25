import numpy as np
from csv import reader
import json
def one_step_creative(M,p4,A_0,A_1):
    j=0
    for i in A_0:
        A_0[j]=p4[i]
        j=j+1
    j=0
    for i in A_1:
        A_1[j]=p4[i]
        j=j+1

    g=set()
    for i in A_1:
        g.add(i)
    g=list(g)
    j=0
    k={}
    for i in g:
        b=A_1.count(i)
        b=1/b
        k[i]=b
    
    for i in range(len(A_1)):
        M[A_0[i]][A_1[i]]=k[A_1[i]]
    
    return M



with open("C:\\surface\\Study\\数模\\2021D\\2021_ICM_Problem_D_Data\\influence_data.csv",'rt',encoding='UTF-8')as raw_data:
    readers=reader(raw_data,delimiter=',')
    x=list(readers)
del x[0]
data=np.array(x)
A_0=data[:,0]
A_1=data[:,4]
p1=set()
for i in A_0:
    p1.add(i)
for i in A_1:
    p1.add(i)
p2=list(p1)
p2=[int(x) for x in p2]
p2=sorted(p2,reverse=False)
t_0=len(p2)
p4={}
#p2=[str(x) for x in p2]
j=0
for i in p2:
    p4[i]=j
    j=j+1
M=np.zeros((t_0,t_0))
A_0=list(A_0)
A_1=list(A_1)
A_0=[int(x) for x in A_0]
A_1=[int(x) for x in A_1]
#p4为对照表，M为一步转移矩阵，A_0和A_1为影响者和追随者
with open('1.json','w')as f1:
    json.dump(p4,f1)

M=one_step_creative(M,p4,A_0,A_1)
hu={}

with open("C:\\Users\\47257\\Desktop\\16.json",'r')as f1:
        gt=json.load(f1)

for i in range(1,51,1):
    print(i)
    d=i/100
    n=t_0
    I=np.ones((n,1))
    Rt=(1/n)*I
    for i in range(100):
        Rt=np.dot(d*M,Rt)+((1-d)/n)*I
    Rt=list(Rt)
    Rt=[float(i) for i in Rt]
    
    Rt=[float(i) for i in Rt]
    uo={}
    for i in range(len(Rt)):
        for j,k in p4.items():
            if i==k:
                uo[f'{j}']=Rt[i]
    yu=len(uo)
    pik=0
    for j in uo.keys():
        if(uo[j]!=gt[j]):
            pik=pik+1
    wr=pik/yu
    hu[f'{d}']=wr
    '''
    with open('C:\\Users\\47257\\Desktop\\use\\1.json','w')as f1:
        json.dump(uo,f1)
    print(uo)
    '''
    '''
    #Rt=[double(x) for x in Rt]
    Y=sorted(Rt,reverse=True)
    F=Y[0:10]
    #F=max(Rt)
    T=[]
    for i in range(len(F)):
        F_0=Rt.index(F[i])
        T.append(F_0)
    T_0=[]
    h=0
    for to in T:
        for i,j in p4.items():
            if j==to:
                T_0.append([i,F[h]])
                h=h+1
                break
    hu[f'{d}']=T_0
    '''

with open("C:\\Users\\47257\\Desktop\\19.json",'w')as f1:
        json.dump(hu,f1)
print(1)

