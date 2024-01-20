from numpy import loadtxt,power,ones
import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from iminuit.cost import LeastSquares

def model( x , a , b, c, d , e):
    return a*power(x,4)+b*power(x,3)+c*power(x,2)+d*x+e

sample = loadtxt('dati.txt')
print(sample)
x = []
y =[]
for i in sample:
    x.append(i[0])
    y.append(i[1])

print(x,y)

plt.plot( x , y , 'silver')
plt.plot( x , y , 'ro' )
plt.xlabel('ml aggiunti')
plt.ylabel('pH')
plt.savefig('plot.png')

#cost = LeastSquares( x , y , 0.01*ones(len(x)) , model )
#a = Minuit( cost , 0 , 0 , 0 , 0 , 0)
#a.migrad()
#a.hesse()
#print(a)
