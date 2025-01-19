# Program to implement logistic regressionocally weighted linear regression 
import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as sk
import seaborn as sns
from math import exp,sin

# x,y= sk.make_friedman1(200,5)
# x=np.c_[[1]*200,x]
# # print(x)

# x,y=[],[]
# file= open('Weighted_reg_1.csv','r')
# for i in file:
#     try:
#         l= list(map(float,i.split(',')))
#         x.append(l[:-1])
#         y.append(float(l[-1]))
#     except:
#         pass
# file.close()
# x,y=np.c_[[1]*244,x],np.array(y)

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
x,y=np.c_[[1]*10407,x],np.array(y)
x_test,y_test= x[10400:],y[10400:]



def find(X):
    # w= x.copy()
    tau=0.01
    w= ((X-x)**2)
    w= np.array([sum(i) for i in w])
    w= np.exp((w**(0.5))/2*tau**2)
    w= np.diag(w)

    xt=np.transpose(x)
    xi=np.linalg.inv(np.dot(xt,x))
    theta= np.dot(xt,w)
    theta=np.dot(theta,x)
    theta=np.linalg.inv(theta)
    theta=np.dot(np.dot(theta,xt),w)
    theta= np.dot(theta,y)
    return np.dot(X,theta)

# print(find(x[5]))
# print(y[5])
x__= np.array([i for i in range(1,len(x_test)+1)])
solution= np.array([find(i) for i in x_test])
plt.scatter(x__,y_test)
plt.scatter(x__,solution)
plt.show()