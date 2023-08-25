import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
def init():
    iris = datasets.load_iris()
    iris=iris['data']
    one=np.ones([50,1])
    setosa=iris[0:50]
    versicolor=iris[50:100]
#    fig,ax=plt.subplots()

    s=[setosa,one]
    setosa=np.column_stack(s)
    one=one*-1
    s=[versicolor,one]
    versicolor=np.column_stack(s)
    plt.hist(versicolor[:,3], bins=30, rwidth=0.9, density=True)
    plt.show()
    setosa_train=setosa[0:40]
    setosa_test=setosa[40:50]
    versicolor_train=versicolor[0:40]
    versicolor_test=versicolor[40:50]
    a=[setosa_train,versicolor_train]
    b=[setosa_test,versicolor_test]
    trainset=np.row_stack(a)
    testset=np.row_stack(b)
    np.random.shuffle(trainset)
    np.random.shuffle(testset)
    return [trainset,testset]
def main():
    trainset,testset=init()
main()
    