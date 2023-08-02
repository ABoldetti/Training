import numpy as np
from matplotlib import pyplot as py

#linea per fare l'istogramma
x=[1,2,3,4,5,6,3,3,3,5,4,2,5,5,3,2,5,6,4,2,3,3,3,5,3]
py.hist(x,bins=int(np.std(x)), alpha=0.5,density=True,)
py.show()

#codice per fare il grafico di gauss
h=1./np.std(x)/np.sqrt(2)
z=x-np.mean(x)
np.exp(-np.power(h*z, 2.)) *h / np.sqrt(np.pi)

