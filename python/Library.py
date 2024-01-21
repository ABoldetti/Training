
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.stats import norm , expon


class Stats:
    def __init__(self, data: list) -> None:
        self.data = data

        #class containing all the main statistical functions
        
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
        
        # class containing all the principal, non-banal function to generate pseudo random number following certain conditions
        
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
    
    def montecarlo(  f , xmax , xmin ,  N=1000 , *args , **kwargs ):
        mu = np.mean( f( np.linspace(xmin , xmax , N) , *args , **kwargs) )
        var = np.std( f( np.linspace(xmin , xmax , N) , *args , **kwargs) )
        return (xmax-xmin)*mu , abs(var)/np.sqrt(N)
    
    def poisson( N:int = 1000, xmin:float = 0 ,  M:int  = 1000 , la:float = 20 ):
        if xmin < 0:
            print( "ERROR" )
            return 0 
        else:
            data = []
            xmax = xmin+(la*N)
            exp = pdfs.exp
            a = myrand.TAC( exp , xmax , xmin , exp(0) , exp(xmin) , M )
            print('diocane')
            for i in range( xmin , xmax , la):
                n = 0
                for j in a:
                    print( j , i )
                    if i < j < i+la:
                        n+=1
                data.append(n)
            return data


class pdfs:
    def __init__(self) -> None:
        
        #class containing some pdfs and cdfs, the func variable is a bool variable that makes the function switch between pdfs and cdfs

        pass
    def gauss( x , mu=0 , sigma=1 , n=1 , func=True) :
        if func:
            return n*norm.pdf( x , loc=mu , scale=sigma)
        else :
            return n*norm.cdf( x , loc=mu , scale = sigma)
    
    def exp ( x , mu = 0 ,tau = 1 , n = 1, func = True):
        if func:
            return n*expon.pdf( x , loc = mu , scale = tau)
        else :
            return n*expon.cdf( x , loc = mu , scale = tau)
    




if __name__ == '__main__':
    plt.hist(myrand.poisson())
    # plt.plot ( np.linspace(-10 , 10 , 1000) , pdfs.exp(np.linspace(-10 , 10 , 1000) , 0))
    # plt.plot ( np.ones(100) , np.linspace( -2 , 2 , 100))
    plt.show()