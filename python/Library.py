
import matplotlib.pyplot as plt
import random
import numpy as np


class stats:
    def __init__(self, data: list) -> None:
        self.data = data

        #statistical function all calculated at the start of the function
        
        self.mean = float(sum(self.data))/len(self.data)
        self.variance = sum( map( (lambda x : (x-self.mean)**2) , self.data)) / (len(self.data)-1)
        self.stdev = np.sqrt(self.variance)
        self.skewness = sum( map( (lambda x : (x-self.mean)**3) , self.data)) / self.stdev
        self.kurtosis = sum( map( (lambda x : (x-self.mean)**4) , self.data)) / self.stdev 
        pass

    def append(self,x):
        self.data.append(x)
        self.__init__(self.data)
    def hist(self):
        plt.xlabel('data')
        plt.hist( self.data , bins= int(np.ceil( 1 + 3.322 * np.log(len(self.data)))) , density = True)
        plt.show()
    def Sturges(x:int):
        return int(np.ceil( 1 + 3.322 * np.log(x)))
    def stats(self):
        print(f""" MEAN: \t {self.mean}
STANDARD DEV: \t {self.stdev}
SKEWNESS: \t {self.skewness}
KURTOSIS: \t {self.kurtosis}""")
        
class myrand:
    def __init__(self) -> None:
        pass
    def TAC( f ,xmax , xmin , ymax , ymin  , N = 1000 , *args , **kwargs):
        vec = []
        while ( len(vec)<N ):
            x = xmin + random.random()*(xmax-xmin)
            y = ymin + random.random()*(ymax-ymin)
            if y < f(x , *args , **kwargs):
                vec.append(x)
        return vec
    
    def CLT( N:int , M:int , mu = .5 , si = .5):
        vec = []
        
        while len(vec) < N:
            a = 0
            for i in range(M):
                a+=(2*si)*random.random()+mu-si
            vec.append(a/M)
        return vec
    
    def HoM( f , xmax , xmin , ymax , ymin , N=1000 , *args , **kwargs):
        n = 0
        A = (xmax - xmin)*(ymax - ymin )
        for i in range(N):
            x = xmin + random.random()*(xmax-xmin)
            y = ymin + random.random()*(ymax-ymin)
            if y < f(x , *args , **kwargs):
                n+=1
        return [ A*n/N , (A/N)*(n/N)*(1-(n/N))]
    
    def Montecarlo(  f , xmax , xmin , ymax , ymin , N=1000 , *args , **kwargs ):
        return 0



if __name__ == '__main__':
    plt.hist(myrand.CLT( 1000 , 1000 , 4 , 0.7))
    plt.show()

