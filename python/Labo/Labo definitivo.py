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

        self.path = path
        # self.round = int( input( "Quante cifre significative si vogliono avere nei risultati? \t" ) )
        self.round = 3
        ausy = path.split(".")
        if ausy[len(ausy)-1] == 'csv':
            self.csv = True
            self.data=pp.read_csv( path )
            self.n_col=len(self.data.columns)
        elif ausy[len(ausy)-1] == 'xlsx':
            self.csv = False
            self.wb = xlsx.excel( path )
            self.count = 0
        pass
    
    def data_analysis (self) :
        if self.csv :
            if self.n_col == 1 :
                self.one_column()
                
            elif self.n_col ==2 :
                self.two_column()
                
            elif self.n_col ==3 :
                self.three_column()
        else :
            for self.table in self.wb.ws.tables.values() :
                self.count += 1
                ausy = self.wb.rolling_table( str(self.table) )
                self.data = ausy.get("data")
                self.coordinates = ausy.get("coordinates")
                self.n_col=len(self.data.columns)
                if self.n_col == 1 :
                    self.one_column()
                    
                elif self.n_col ==2 :
                    self.two_column()
                    
                elif self.n_col ==3 :
                    self.three_column()

    def one_column( self ):

        x = np.array(self.data.values)
        chi = np.sum( np.power( ( np.mean( x ) - x ) , 2 ) / np.power( stdev( x ) , 2 ) )
        
        self.gaussian( x )
        
        # modo per selezionare se dare l'input sul terminale o sul file excel
        if self.csv:

            string = f"$ \chi: {round(chi,self.round)} , media: {round(np.mean(x),self.round)}$"
            print( string )
            plt.show()

        else :

            letter = ord(self.coordinates[0])
            number = self.coordinates[1]
            #scrittura dei vari valori nelle celle sottostanti la tabella
            self.wb.ws[f"{chr(letter)}{number+1}"] = "chi:"
            self.wb.ws[f"{chr(letter+1)}{number+1}"] = round( chi , self.round)
            self.wb.ws[f"{chr(letter)}{number+2}"] = "media :"
            self.wb.ws[f"{chr(letter+1)}{number+2}"] = round(np.mean(x),self.round)
            plt.savefig( f"Tabella{self.count}.jpg" )
            self.wb.ws.add_image(f"Tabella{self.count}.jpg" , f"{chr(letter+4)}{number}")
            self.wb.wb.save(self.path)


    def two_column( self ):

        x = np.array( self.data[ self.data.columns[ 0 ] ].values )
        y = np.array( self.data[ self.data.columns[ 1 ] ].values )
        sy = float( input( "Inserire valore dell'incertezza su y: \t" ) )
        a = i.interpolazione( x , y , sy )
        b = a.Lineare()
        A = b.get( "A value" )
        sA = b.get( "A error" )
        B = b.get( "B value" )
        sB = b.get( "B error" )
        chi = np.sum( np.power( ( ( y - A * x - B ) / sy) , 2))
        self.linear_regression( x , y , sy, A , B )
        
        if self.csv:
            string = f"""$\chi:{chi}$
                    $equazione: ({round(A,self.round)}\pm{round(sA,self.round)})x + ({round(B,self.round)}\pm{round(sB,self.round)})$"""
            print( string )
            plt.show()
        else :
            letter = ord(self.coordinates[0])
            number = self.coordinates[1]
            #scrittura dei vari valori nelle celle sottostanti la tabella
            self.wb.ws[f"""{chr(letter)}{number+1}"""] = "chi:"
            self.wb.ws[f"""{chr(letter+1)}{number+1}"""] = round( chi , self.round)
            self.wb.ws[f"""{chr(letter)}{number+2}"""] = "A :"
            self.wb.ws[f"""{chr(letter+1)}{number+2}"""] = f"{round( A , self.round)}" + "+" + f"{round( sA , self.round)}"
            self.wb.ws[f"""{chr(letter)}{number+3}"""] = "B:"
            self.wb.ws[f"""{chr(letter+1)}{number+3}"""] = f"{round( B , self.round)}" + "+" + f"{round( sB , self.round)}"
            #salvataggio del grafico sottoforma jpg e caricamento del file jpg nell'excel
            plt.savefig(f"table{self.count}.jpg")
            # self.wb.ws.add_image( f"Tabella{self.count}.jpg" , anchor=f"{chr(letter+4)}{number}" )
            self.wb.wb.save(self.path)

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
        self.weighted_linear_regression( x , y , sy, A , B )
        plt.xlabel( self.data.columns[0] )
        plt.ylabel( self.data.columns[1] )
        # modo per selezionare dove mettere
        if self.csv:
            string = f"""$\chi:{chi}$
                $equazione: ({round(A,self.round)}\pm{round(sA,self.round)})x + ({round(B,self.round)}\pm{round(sB,self.round)})$
                $\sigma_AB :{sAB}$"""
            print( string )
            plt.show()
        else :
            letter = ord(self.coordinates[0])
            number = self.coordinates[1]
            #scrittura dei vari valori nelle celle sottostanti la tabella
            self.wb.ws[f"""{chr(letter)}{number+1}"""] = "chi:"
            self.wb.ws[f"""{chr(letter+1)}{number+1}"""] = round( chi , self.round)
            self.wb.ws[f"""{chr(letter)}{number+2}"""] = "A :"
            self.wb.ws[f"""{chr(letter+1)}{number+2}"""] = f"{round( A , self.round)}" + "+" + f"{round( sA , self.round)}"
            self.wb.ws[f"""{chr(letter)}{number+3}"""] = "B:"
            self.wb.ws[f"""{chr(letter+1)}{number+3}"""] = f"{round( B , self.round)}" + "+" + f"{round( sB , self.round)}"
            self.wb.ws[f"""{chr(letter)}{number+4}"""] = "Covarianza:"
            self.wb.ws[f"""{chr(letter+1)}{number+4}"""] = sAB
            #salvataggio del grafico sottoforma jpg e caricamento del file jpg nell'excel
            plt.savefig(f"table{self.count}.jpg")
            self.wb.ws.add_image(f"Tabella{self.count}.jpg" , f"{chr(letter+4)}{number}")
            self.wb.wb.save(self.path)


# Funzioni per i grafici di matplotlib
    def gaussian( self , vec: np.array ) :

        plt.xlabel( self.data.columns[0] )
        plt.hist( vec , bins= int( np.size( vec )/stdev(vec) ) , density = True)
        span = np.linspace( min(vec), max(vec))
        plt.plot( span , gauss( span , stdev(vec) ))

        

    def linear_regression( self , x: np.array , y: np.array, sy: float, A: float, B: float ):

        plt.xlabel( self.data.columns[0] )
        plt.ylabel( self.data.columns[1] )
        plt.errorbar( x , y , sy*np.ones( np.size( x ) ) , fmt='o', capsize=4, color='red', ecolor='black')
        plt.plot( x , line( x ,A , B))
        

    def weighted_linear_regression( self , x: np.array , y: np.array, sy: np.array, A: float, B: float ):
        
        plt.xlabel( self.data.columns[0] )
        plt.ylabel( self.data.columns[1] )
        plt.errorbar( x , y , sy , fmt='o')
        plt.plot( x , line( x , A , B ))
        plt.show()

    def error_prop( self , formula: str ) :
        ep.propagazione_errore()

#funzioni per disegnare retta e gaussiana
def stdev( x : np.array ) :
        if np.size( x ) <20:
            a=np.sqrt( np.sum(( np.mean(x) - x )**2)/(np.size(x)-1))
        else:
            a=np.sqrt( np.sum((np.mean(x)- x)**2)/np.size(x) )
        return a
    
def gauss( x: np.array , sx : float) -> np.array:
        n = x - np.average( x )
        d = 2 * sx**2
        y = 1 / ( np.sqrt( 2 * np.pi ) * sx ) * np.exp( -0.5 * np.power( n , 2 ) / d )
        return y
def line ( x: np.array , A: float , B: float ) -> np.array:
    return A*x + B
    
if __name__ == '__main__' :
    a=labo( '/Users/andreaboldetti/Documents/GitHub/My_first_Repository/trial.xlsx' )
    # x = np.linspace(0,5,6)
    # y = np.array([0.1, 0.3, 0.6, 0.7,0.9, 1.3])
    # sy=0.1
    # b = i.interpolazione( x ,y , sy )
    # c = b.Lineare()
    # #a.linear_regression( x , y , sy, c.get("A value") , c.get("B value") )
    # a.gaussian(x)
    a.data_analysis()
    # a = np.array([ 0.1,0.4,0.6,0.4,0.5,0.4,0.3,0.5,0.8,0.2,0.4])
    # print(  np.sum(( np.mean(a) - a )**2)/(np.size(a)-1)) 
    # print( stdev( a ))