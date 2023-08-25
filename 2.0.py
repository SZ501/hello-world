import numpy as np
from sklearn import datasets
def init():
    iris = datasets.load_iris()
    iris=iris['data']
    one=np.ones([50,1])
    setosa=iris[0:50]
    versicolor=iris[50:100]

    s=[setosa,one]
    setosa=np.column_stack(s)
    one=one*-1
    s=[versicolor,one]
    versicolor=np.column_stack(s)

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
def train(trainset,testset):
    η=1
    w0=np.zeros([4,1])
    b0=np.zeros([1,1])
    for i in range(100):  
        index_0=np.random.randint(0,80)
        y=trainset[index_0][-1].reshape(1,1)
        x=trainset[index_0][0:-1].reshape(1,4)
        if(y*(np.dot(x,w0)+b0))<=0:
            w0=w0+η*(x.T*y)
            b0=b0+η*y
    return [w0,b0]
def test(w,b,testset):
    correct=0
    wrong=0
    for i in testset:
        x=i[0:-1].reshape(1,4)
        y=i[-1].reshape(1,1)
        if(y*(np.dot(x,w)+b))<=0:
            wrong=wrong+1
        else:
            correct=correct+1
    return [correct,wrong]
def main():
    trainset,testset=init()
    w,b=train(trainset,testset)
    correct,wrong=test(w,b,testset)
    print(f'correct:{correct}')
    print(f'wrong:{wrong}')
main()