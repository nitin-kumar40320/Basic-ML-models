# program to implement linear regression using matrices and hence generalise

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes 
# da=load_diabetes()
# x,y=da.data,np.array(da.target)
# x=np.c_[[1]*442,x]

x,y=[],[]
file= open('regression_2.csv','r')
for i in file:
    try:
        l= list(map(float,i.split(',')))
        x.append(l[1:-1])
        y.append(float(l[-1]))
    except:
        pass
file.close()
# print(x,len(x))
x,y=np.c_[[1]*10407,x],np.array(y)
x_test,y_test=x[9000:],y[9000:]
x,y=x[:9000],y[:9000]

def train(x,y):
    xt=np.transpose(x)
    xi=np.linalg.inv(np.dot(xt,x))
    theta=np.dot(xi,xt)
    theta= np.dot(theta,y)
    return theta

def predict(theta,x):
    y=np.dot(x,theta)
    return y
    # plt.plot(y)

plt.scatter(np.array([i for i in range(len(y_test))]),y_test)
y_pred= predict(train(x,y),x_test)
plt.scatter(np.array([i for i in range(len(y_pred))]),y_pred)
wrong=0
for i in range(len(y_test)):
    if abs(y_test[i]-y_pred[i])>1:
        wrong+=1
print("wrong predictions=",wrong)
print("Right predictions=",len(y_test)-wrong)
plt.show()
