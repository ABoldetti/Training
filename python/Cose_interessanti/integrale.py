import numpy as np
import matplotlib.pyplot as plt


def integral(f, a, b, n):
    if a == -np.inf:
        a = -1e10
    if b == np.inf:
        b = 1e10
    dx = (b-a)/n
    s = 0
    #print( dx )
    for i in range( n ):
        c = a + i*dx
        d = a + (i+1)*dx
        
        #print( dx , c , d , f(c) , f(d) ) 

        s+= abs(f(c) - f(d))*dx
    return s

def f(x , t , x0):
    return np.exp( - np.power((x - x0),2) / (8*t) + t - x0**2)

if __name__ == "__main__":
    x = []
    y = []
    for i in range(100):
        for j in range(1,100):
            ausy = []
            ausy.append( integral( lambda x : f( i , -1/j , x) , -np.inf , np.inf , int(100)) )
            x.append(i)
            y.append(np.mean(ausy))
    plt.plot(x,y)
    plt.show()