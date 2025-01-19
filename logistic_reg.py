# Program to implement the logistic regression
# importing the required libraries
import numpy as np
import sklearn.datasets as sk
import matplotlib.pyplot as plt
from math import exp

# IMPORTING THE DATA FOR TRAINING AND TESTING

# da= sk.load_breast_cancer()
# x,y= da.data[:100],da.target[:100]
# x=np.c_[[1]*100,x]

# x,y=[],[]
# file= open('logical_reg_1.csv','r')
# for i in file:
#     try:
#         l= list(map(float,i.split(',')))
#         x.append([l[1]]+l[3:])
#         y.append(float(l[2]))
#     except:
#         pass
# file.close()
# x,y=np.c_[[1]*512,x],np.array(y)

# x,y=[],[]
# file= open('logical_reg_2.csv','r')
# for i in file:
#     try:
#         l= list(map(float,i.split(',')))
#         x.append(l[:-1])
#         y.append(float(l[-1]))
#     except:
#         pass
# file.close()
# print(len(x),len(y))
# x,y=np.c_[[1]*2338,x],np.array(y)
# xp,yp=x[100:200],y[100:200]
# x,y=x[:100],y[:100]
# print(len(x[0]))

# we define the softmax function which takes the value of x and theta as row matrices
def h(x,theta):
    temp= np.transpose(theta)
    return 1/(1+np.exp(-np.dot(x,temp)))     # and it returns a 

def train(x,y):
    theta= np.matrix([0]*14)
    alp=0.1
    step=10000
    counter=0
    print(theta)
    print() 

    while  step>0 and counter<100 :
        thetaprev= theta.copy()
        h_= np.matrix([h(j,theta) for j in x])
        h_= np.transpose(y-h_)
        # print(h_,'*')
        for i in range(14):
            x_=x[:,i]
            x_= np.dot(x_,h_)
            theta[i]+=alp*x_
        print(theta)
        step= sum(abs(theta-thetaprev))
        print(step)
        print()
        if counter>20:
            alp-=0.01
        counter+=1
    return theta

arbitrary= np.array([i for i in range(1,101)])
plt.scatter(arbitrary,yp)
# print("*")
th= train(x,y)
# print("**")
predicted=[]
for i in xp:
    predicted.append((h(i,th)))
predicted= np.array(predicted)
# print("***")
plt.scatter(arbitrary,predicted)
yp= list(yp-predicted)
print(len(yp)-yp.count(0))
# print(predicted)
plt.show()