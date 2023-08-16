#Labo definitivo
import numpy as np
import pandas as pp
import scipy.stats as ss
import matplotlib.pyplot as plt

# file secondari
import Interpolazione as i
import Err_prop as ep
import Excel_plugin as xlsx

#come input della classe inserire il percorso del file csv, poi eseguire il la funzione data analysis

#la funzione 'gauss' ha problemi con la formula della gaussiana, la fa troppo schiacciata
#la funzione di propagazione dell'errore devo ancora capire come farla. SEGNARE OGNI IDEA


class labo:
    def __init__(self, path: str):
        ausy = path.split(".")
        if ausy[len(ausy)-1] == 'csv':
            self.csv = True
            self.data=pp.read_csv( path )
            self.n_col=len(self.data.columns)
        elif ausy[len(ausy)-1] == 'xlsx':
            self.csv = False
            self.wb = xlsx.excel( path )
        pass
    
    def stdev( self, x : np.array ) :

        if np.size( x ) <20:
            a=np.sqrt( np.sum(( np.mean(x)- x )**2)/np.size(x)-1)
        else:
            a=np.sqrt( np.sum((np.mean(x)- x)**2)/np.size(x) )
        return a
    
    def data_analysis (self) :
        if self.csv :
            if self.n_col == 1 :
                self.one_column()
                
            elif self.n_col ==2 :
                self.two_column()
                
            elif self.n_col ==3 :
                self.three_column()
        else :
            for table in range( 1 , len( self.ws.tables.values()+1 ) ) :
                self.data = self.wb.rolling_table( table )
                self.n_col=len(self.data.columns)
    def one_column( self ):

        x = np.array(self.data.values)
        chi = np.sum( np.power( ( np.mean( x ) - x ) , 2 ) / np.power( self.stdev( x ) , 2 ) )
        string = f"""$ \chi: {round(chi,3)} , media: {round(np.mean(x),3)}$"""
        self.gaussian( x )

    def two_column( self ):

        x = np.array( self.data[ self.data.columns[ 0 ] ].values )
        y = np.array( self.data[ self.data.columns[ 1 ] ].values )
        sy = float( input( "Inserire valore dell'incertezza su y" ) )
        a = i.interpolazione( x , y , sy )
        b = a.Lineare()
        A = b.get( "A value" )
        sA = b.get( "A error" )
        B = b.get( "B value" )
        sB = b.get( "B error" )
        chi = np.sum( np.power( ( ( y - A * x - B ) / sy) , 2))
        string = f"""$\chi:{chi}$
                $equazione: ({round(A,3)}\pm{round(sA,3)})x + ({round(B,3)}\pm{round(sB,3)})$"""
        plt.title( string )
        self.linear_regression( x , y , sy, A , B )

    def three_column( self ):

        x = np.array( self.data[ self.data.columns [0] ].values )
        y = np.array( self.data[ self.data.columns [1] ].values )
        sy = np.array( self.data[ self.data.columns[2] ].values )
        a = i.interpolazione( x , y , sy )
        b = a.Pesata()
        A = b.get( "A value" )
        sA = b.get( "A error" )
        B = b.get( "B value" )
        sB = b.get( "B error" )
        sAB = b.get( "coveriant" )
        chi = np.sum( ( ( y-A*x-B ) / sy ) **2 )
        stringa = f"""$\chi:{chi}$
                $equazione: ({round(A,3)}\pm{round(sA,3)})x + ({round(B,3)}\pm{round(sB,3)})$
                $\sigma_AB :{sAB}$"""
        plt.title( stringa )
        self.weighted_linear_regression( x , y , sy, A , B )


            
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

    def error_prop( self , formula: str ) :
        ep.propagazione_errore()

#funzioni per disegnare retta e gaussiana
def gauss( x: np.array , sx : float) -> np.array:
        n = x - np.average( x )
        d = 2 * sx**2
        y = 1 / ( np.sqrt( 2 * np.pi ) * sx ) * np.exp( -0.5 * np.power( n , 2 ) / d )
        return y
def line ( x: np.array , A: float , B: float ) -> np.array:
    return A*x + B
    
if __name__ == '__main__' :
    a=labo( 'python\data.csv' )
    # x = np.linspace(0,5,6)
    # y = np.array([0.1, 0.3, 0.6, 0.7,0.9, 1.3])
    # sy=0.1
    # b = i.interpolazione( x ,y , sy )
    # c = b.Lineare()
    # #a.linear_regression( x , y , sy, c.get("A value") , c.get("B value") )
    # a.gaussian(x)
    a.data_analysis()
