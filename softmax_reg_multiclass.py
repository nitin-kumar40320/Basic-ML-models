import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as sk
from math import exp

# importing data
da= sk.load_wine()
x,y=da.data,da.target
test_size= int(len(x)*0.8)
x_test,y_test=x[test_size:],y[test_size:]
x,y=list(x[:test_size]),y[:test_size]
x= np.c_[[1]*142,x]
# preparing y as a matrix output(in 1 hot representation)
ytemp= y.copy()
y=[]
for i in range(len(ytemp)):
    y.append([0,0,0])
    y[i][ytemp[i]]=1


def h(x,theta):
    n= len(x)
    eta= np.dot(np.transpose(theta),x)
    ans= np.transpose(np.exp(eta))
    ans= ans.astype(float)
    for i in range(n):
        s= sum(ans[i])
        ans[i]/=s
    return ans

def cost(y_pred,y_true):
    loss= -np.log(np.dot(y_pred,y_true))
    return np.sum(loss)

def multiclass_train(x,y):
    n= len(x)
    k=len(y[0])
    f= len(x[0])
    theta= np.array([[1]*k]*f)
    alp=0.01
    counter=0

    while cost>10 and counter<100:
        
    

    
# multiclass_train(x,y)
# xplot=[i for i in range(1,len(x_test)+1)]
xplot=np.arrange(1,len(x_test)+1)
predicted_test=[]
for i in x_test:
    predicted_test.append(multiclass_train)

counter=0
for i in range(len(y_test)):
    if y_test[i]!=predicted_test[i]:
        counter+=1
print(f"{counter} are wrong out of {len(y_test)}")
# plt.scatter(xplot,y_test)
# plt.scatter(xplot,predicted_test)
# plt.show()