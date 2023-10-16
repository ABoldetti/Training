import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import rcParams
import os


#linea per fare l'istogramma
x=[1,2,3,4,5,6,3,3,3,5,4,2,5,5,3,2,5,6,4,2,3,3,3,5,3]
plt.hist(x,bins=int(np.std(x)), alpha=0.5,density=True,)

dir_name = 'C:/Temp'
# rcParams['savefig.directory'] = dir_name
# print( rcParams['savefig.directory'])
# plt.rc( 'savefig' , directory=dir_name)

plt.savefig("C:/Temp/prova.png")

c = os.path.isdir
