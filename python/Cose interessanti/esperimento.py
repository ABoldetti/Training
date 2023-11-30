import numpy as np
import matplotlib.pyplot as plt

class stats:
    def __init__(self, data: list) -> None:
        self.data = data
        pass
    def append(self,x):
        self.data.append(x)
    def mean(self):
        return float(sum(self.data))/len(self.data)
    def stdev(self):
        return np.sqrt(self.variance())
    def variance(self):
        return sum( map( (lambda x : ((x-self.mean())**2)) , self.data)) / (len(self.data)-1) 
    def skewness(self):
        return sum( map( (lambda x : ((x-self.mean())**3)) , self.data)) / ((len(self.data)-1)*(self.stdev())**3) 
    def kurtosis(self):
        return sum( map( (lambda x : ((x-self.mean())**4)) , self.data)) / ((len(self.data)-1)*(self.stdev())**4) 
    def hist(self):
        plt.xlabel('data')
        plt.hist( self.data , bins= int(np.ceil( 1 + 3.322 * np.log(len(self.data)))) , density = True)
        plt.show()
    def stats(self):
        print(f""" MEAN: \t {self.mean()}
STANDARD DEV: \t {self.stdev()}
SKEWNESS: \t {self.skewness()}
KURTOSIS: \t {self.kurtosis()}""")
        self.hist()
    

if __name__ == '__main__':
    data = []
    for i in range(1000000):
        x,y = np.random.normal( 0 , 1 , 2)
        if x>y :
            data.append(x)
        else: data.append(y)
    a = stats(data)
    a.stats()