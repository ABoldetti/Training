#Labo definitivo
import numpy as np
import pandas as pp
import scipy.stats as ss
import matplotlib.pyplot as plt
import Interpolazione as i

#il file CSV deve avere come prima colonna il nome VALUE nel caso in cui sia un istogramma,
#nella seconda colonna nel caso in cui sia un'interpolazione

#

def gauss( x: np.array , sx : float) -> np.array:
        n = x - np.average( x )
        d = 2 * sx**2
        y = 1 / ( np.sqrt( 2 * np.pi ) * sx ) * np.exp( -0.5 * np.power( n , 2 ) / d )
        return y
def line ( x: np.array , A: float , B: float ) -> np.array:
    return A*x + B
def bins ( x: np.array ):
    return np.sqrt( np.size( x ) )

class labo:
    def __init__(self):
        self.data=pp.read_csv("/Users/andreaboldetti/Documents/GitHub/My_first_Repository/python/data.csv")
        self.n_col=len(self.data.columns)
        pass
    def stdev( self, x : np.array ) :
        if np.size( x ) <20:
            a=np.sqrt( np.sum(( np.mean(x)- x )**2)/np.size(x)-1)
        else:
            a=np.sqrt( np.sum((np.mean(x)- x)**2)/np.size(x) )
        return a
    def one_column( self ):

        x = np.array(self.data.values)
        chi = np.sum( np.power( ( np.mean( x ) - x ) , 2 ) / np.power( self.stdev( x ) , 2 ) )
        ss.chi2.cdf( chi , np.size( x ) - 3 )
        self.gaussian( x )

    def two_column( self ):

        x = np.array(self.data[ self.data.columns [0]].values)
        y = np.array(self.data[ self.data.columns[1]].values)
        sy = float(input("Inserire valore dell'incertezza su y"))
        a = i.interpolazione( x , y , sy )
        b = a.Lineare()
        A = b.get("A value")
        sA = b.get("A error")
        B = b.get("B value")
        sB = b.get("B error")
        chi = np.sum( np.power( ( ( y - A * x - B ) / sy) , 2))
        plt.title( f"""$\chi:{chi}$
                $equazione: ({round(A,3)}\pm{round(sA,3)})x + ({round(B,3)}\pm{round(sB,3)})$""")
        self.linear_regression( x , y , sy, A , B )

    def three_column( self ):

        x = np.array(self.data[ self.data.columns [0]].values)
        y = np.array(self.data[ self.data.columns [1]].values)
        sy = np.array(self.data[ self.data.columns[2]].values)
        a = i.interpolazione( x , y , sy )
        b = a.Pesata()
        A = b.get("A value")
        sA = b.get("A error")
        B = b.get("B value")
        sB = b.get("B error")
        sAB = b.get("coveriant")
        chi = np.sum( ((y-A*x-B )/sy)**2)
        plt.title( f"""$\chi:{chi}$
                $equazione: ({round(A,3)}\pm{round(sA,3)})x + ({round(B,3)}\pm{round(sB,3)})$
                $\sigma_AB :{sAB}$""")
        self.weighted_linear_regression( x , y , sy, A , B )

    def data_analysis (self) :

        if self.n_col == 1 :
            self.one_column()
            
        elif self.n_col ==2 :
            self.two_column()
            
        elif self.n_col ==3 :
            self.three_column()
            
    def gaussian( self , vec: np.array ) :

        plt.hist( vec , bins= int( np.size( vec )/self.stdev(vec) ) , density = True)
        span = np.linspace( min(vec), max(vec))
        plt.plot( span , gauss( span , self.stdev(vec) ))
        plt.show()

    def linear_regression( self , x: np.array , y: np.array, sy: float, A: float, B: float ):

        plt.errorbar( x , y , sy*np.linspace( min( x ) , max( x ), np.size( x ) ) , fmt='o', capsize=4, color='red', ecolor='black')
        plt.plot( x , line( x ,A , B))
        plt.show()

    def weighted_linear_regression( self , x: np.array , y: np.array, sy: np.array, A: float, B: float ):
        
        plt.errorbar( x , y , sy , fmt='o')
        plt.plot( x , line( x , A , B ))
        plt.show()
    def error_prop( self , formula: str) :
        c=0
    
if __name__ == '__main__' :
    a=labo()
    # x = np.linspace(0,5,6)
    # y = np.array([0.1, 0.3, 0.6, 0.7,0.9, 1.3])
    # sy=0.1
    # b = i.interpolazione( x ,y , sy )
    # c = b.Lineare()
    # #a.linear_regression( x , y , sy, c.get("A value") , c.get("B value") )
    # a.gaussian(x)
    a.data_analysis()
