import matplotlib.pyplot as plt
from numpy import  arange
from math import *
x = [i for i in arange(-30,31,0.1)]
y = [0.0]*len(x)

fun = input("Digite a expressão (n para somatorio dever ser maiusculo N!\n")
fun1=fun.replace("N","(i+1)")
fun2=fun1.replace('x','*x[val]')

for val in range(0,len(x)):
    for i in range (0,2):
        y[val] += eval(fun2)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position(('data', 0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.ylim(-2,2)
plt.xlim(-4,4)
plt.plot(x,y)

plt.show()
