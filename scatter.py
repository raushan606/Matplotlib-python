# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:42:30 2019

@author: raushan kumar
"""

#Scatter Plot
import matplotlib.pyplot as plt

x=[]
m=int(input("Enter range : "))
print('Enter elements for X-axis:')
for i in range(m):
    x.append(eval(input()))
y=[]

print("Enter elements for Y-axis: ")
for j in range(m):
    y.append(eval(input()))
plt.scatter(x,y,color='r')
xaxis=input('Enter X-axis name: ')
yaxis=input('Enter Y-axis name: ')
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.show()