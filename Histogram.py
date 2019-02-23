# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:11:07 2019

@author: raushan kumar
"""

#Histogram

from matplotlib import pyplot as plt
y=[]
m=int(input('Enter range for Y-axis: '))
print('Enter Y-axis elements: ')
for i in range(m):
    y.append(int(input()))
bin=[]

n=int(input('Enter range for X-axis: '))

print('Enter ranges: ')
for j in range(n):
    bin.append(int(input()))
plt.hist(y,bin,histtype='bar',rwidth=0.3,color='blue')
plt.title('Histogram')
xaxis=input("Enter Name for X-axis: ")
yaxis=input("Enter Name for Y-axis: ")
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.show()