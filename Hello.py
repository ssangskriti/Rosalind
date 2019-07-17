import pandas as pn
import numpy as np



print("Hello Python")
print('Hello Joy Bangla')
x=2
print(x+2)
x=3.3
print(x)
if x>0:
    print("This is a positive number")
else:
    print("This is a negative number")

# this is a comment

# list
x=[]
print(x)

x.append(1)
x.append(2)
x.append(3)
x.append(2)
x.append('A')
print(x)

#dictionary

d={}

d["Dhaka"]=0

d["Dinjaput"]=400
d["Chittagong"]=255
d["Dhaka"]=10

print(d["Dhaka"])

for i in range(0,10,2):  # for(int i=0;i<10;i++)
    print(i)

print(x)

for y in x:
    print(y)

X=pn.read_csv("X.csv",header=None)
print(X.shape)
X=np.array(X)
print(X)

y=pn.read_csv("Y.csv",header=None)
y=np.array(y)
print(y)

a=[2,3,4]
a.append(5)
print(a)
a=np.array([2,3,4])
print(a)


import sklearn.neighbors as ng

clf=ng.KNeighborsClassifier(10)
clf.fit(X,y)

i=4009
ypred=clf.predict(X[i,])
print(ypred)
print(y[i])