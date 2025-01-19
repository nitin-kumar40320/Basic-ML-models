import numpy as np
import matplotlib.pyplot as plt

x,y=[],[]
file= open('Salary_dataset.csv','r')
for i in file:
    a,b,c= i.split(',')  
    try:
        x.append(float(b))
        y.append(float(c))
    except:
        pass
file.close()

# function to open the file Salary_dataset.csv 

def solution(x,y) :
    x_,y_=x.copy(),[]
    x= np.array(x)
    y= np.array(y)
    # print(x,y)
    a,b=0,0
    j=0
    for i in range(len(x)):
        j+= (a+(b*x[i])-y[i])**2
    j/=2
    print(j)
    alp=0.0001
    cr=0
    jpre=j+1
    while abs(j)<abs(jpre)  :
        
        apre,bpre= a,b
        # A= (y[cr%30]-a-(b*x[cr%30]))*x[cr%30]
        A=0
        for i in range(len(x)):
            A+= (y[i]-apre-(bpre*x[i]))*x[i]
        a+= alp*A

        # B= (y[cr%30]-a-(b*x[cr%30]))*x[cr%30]
        B=0
        for i in range(len(x)):
            B+= (y[i]-apre-(bpre*x[i]))*x[i]
        b+= alp*B
        cr+=1

        jpre=j
        j=0
        for i in range(len(x)):
            j+= (a+(b*x[i])-y[i])**2
        j/=2
        print(j,jpre)

    a,b=apre,bpre
    print(cr)
    print(a,b)
    for i in range(len(x_)):
        y_.append(a+(b*x_[i]))
    x_,y_= np.array(x_),np.array(y_)

    plt.plot(x,y)
    # print(y,y_)
    plt.plot(x_,y_)
    plt.show()    

solution(x,y)