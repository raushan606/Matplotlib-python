# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:51:38 2019

@author: raushan kumar
"""
from matplotlib import pyplot as plt

#Bar Graph
m=int(input('Range for "X": '))
n=int(input('Range for "Y": '))
x=[]
y=[]
print('Enter the values for X-axis: ')
for i in range(m):
    x.append(int(input()))
print('Enter the value for Y-axis: ')
for j in range(n):
    y.append(int(input()))

xaxis=input('Enter name for X-axis: ')
yaxis=input('Enter name for Y-axis: ')    
plt.bar(x,y,align='center',color='g')
plt.title('Bar Graph')
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.show()
