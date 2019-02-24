import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import style
style.use('ggplot')
#Straight Line
print()
print('For STRAIGHT LINE:')
m=int(input("Enter the value of 'm': "))
c=int(input("Enter the value of 'c': "))

x = np.arange(-10,11) 
y = m *x + c 
plt.title("Straight line") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,'--g',label='Straight line',linewidth=2) 
plt.legend()
plt.show()


#Parabola
print()
print('For PARABOLA:')
a=int(input("Enter the value of 'a': "))
y1=(((4*a*x)**0.5))
plt.title("Parabola")
plt.plot(x,y1,'r',label='Parabola',linewidth=3)
plt.legend()
plt.show()

#Circle
print()
print('For CIRCLE:')
h=int(input("Enter the value of 'h': "))
k=int(input("Enter the value of 'k': "))
r=int(input("Enter the value of 'r': "))
y2=k+(r**2-(x-h)**2)**0.5
plt.title("Circle")
plt.plot(x,y2,'-c',label='Circle',linewidth=3)
plt.legend()

plt.show()