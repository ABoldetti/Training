#Labo definitivo
import numpy as np
import pandas as pp
import scipy.stats as ss
from matplotlib import pyplot as py
import Interpolazione

#il file CSV deve avere come prima colonna il nome VALUE nel caso in cui sia un istogramma,
#nella seconda colonna nel caso in cui sia un'interpolazione

class labo:
    def __init__(self):
        self.data=pp.read_csv("/Users/andreaboldetti/Documents/projects/just-learning/python/data.csv")
        self.n_col=len(self.data.columns)
        pass
    def stdev(x : np.array):
        if len( x ) <20:
            a=np.sqrt( np.sum((np.mean(x)- x)**2)/len(x)-1)
        else:
            a=np.sqrt( np.sum((np.mean(x)- x)**2)/len(x) )
        return a
    def goodness(self):
        #test del chi quadro
        if self.n_col == 1:
            x = self.data.value.to_numpy
            chi = np.sum(((np.mean(x)-x))**2/(labo.stdev(x))**2)
            return ss.chi2.cdf( chi, len(x)-3)
        elif self.n_col == 2:
            x = self.data[ self.data.columns [0]].to_numpy
            y = self.data.value.to_numpy
            sy = input("Inserire valore dell'incertezza su y")
            a=Interpolazione(x,y,sy)
            b=a.Lineare()
            A=b.get("A value")
            B=b.get("B value")
            chi= np.sum( ((y-A*x-B )/sy)**2)
            return ss.chi2.cdf( chi, len(x)-2)
        else:
            x = self.data[ self.data.columns [0]].to_numpy
            y = self.data.value.to_numpy
            sy = self.data[ self.data.columns[2]].to_numpy
            a=Interpolazione(x,y,sy)
            b=a.Pesata()
            A=b.get("A value")
            B=b.get("B value")
            chi= np.sum( ((y-A*x-B )/sy)**2)
            return ss.chi2.cdf( chi, len(x)-2)
    def graphs(self):
        #grafico interpolazione o istogramma determinato dalla bontà dell'adattamento dei dati al valore medio o all'equazione della retta
        print("ciao")
a=labo()
a.goodness()



