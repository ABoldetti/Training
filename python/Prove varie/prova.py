import numpy as np
import scipy as sp
import matplotlib as plt
import pandas as pd

#RICORDA, la potenza in python è ** non ^
a=np.array
m=pd.read_csv("datix.csv")
print(m)
x=m.to_numpy
a=x
media=np.mean(x)
print(m,"\n",a)
print('a=',a,'\n motherfucker',a)
b=np.zeros(5)
print(b)


print(media)
def devstd(x,m):
    d=0
    e=0
    for i in x:
        d=(i-m)^2
    e=np.sqrt(d/(len(x)-1))
    return e

plt.errorbar(a,b, fmt='o', ls='none', label='data')

