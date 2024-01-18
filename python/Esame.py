import numpy as np
import matplotlib.pyplot as plt

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
    def stats(self):
        print(f""" MEAN: \t {self.mean}
STANDARD DEV: \t {self.stdev}
SKEWNESS: \t {self.skewness}
KURTOSIS: \t {self.kurtosis}""")

