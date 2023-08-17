from openpyxl import load_workbook
from openpyxl.worksheet.table import Table
import numpy as np
import pandas as pd


class excel :
    def __init__( self , path: str ) -> None:
        self.wb = load_workbook( path )
        self.ws = self.wb.active
        pass
    def table ( self , data: str) -> list:

        # pls don't touch this code, i don't know how it works. tables.values gives back a shit of a string
        a = str( data )
        b = a.split( "Parameters:" )
        c = list( )
        c = b [ 2 ]
        d = c.split( "," )
        h = d [ 0 ]
        e = h [ slice ( 6 , len( h ) -1 ) ]
        return e.split ( ":" )

    def accumulating_data ( self , coordinates :list ) ->  pd.DataFrame:
        ausy = list()
        df = pd.DataFrame(ausy)
        print( coordinates )
        for i in range( ord( coordinates [ 0 ] ) , ord( coordinates [ 2 ] ) ):
            print( i , "\n" )
            ausy = list()
            for j in range( coordinates [ 1 ] + 1 , coordinates [ 3 ]+1 ):
                ausy.append( (self.ws[f"""{chr(i)}{j}"""].value) )
            df[ str(self.ws[f"""{chr(i)}{coordinates[1]}"""].value) ] = pd.DataFrame(ausy)
        print(df)
        return(df)
    
    #funzione che, date le coordinate attaccate, le splitta in parte letterale e parte numerica
    def getting_coordinates ( self , set :list ) -> list :
        a = list()
        for i in range( len( set ) ):
            ausy = 0
            for j in range( len( set[i] ) ):
                if ord( set[i][j] ) < 65:
                    ausy = j
                    break
            n = int(set[ i ][ slice( j , len( set [ i ] ) ) ])
            char = set[ i ][ slice( j ) ]
            a.append( char )
            a.append( n )
        return a
    
    def elaborating_coordinates( self , coordinates: list ):
        return [ coordinates[ 0 ] , coordinates[ len(coordinates)-1 ] + 2 ]

        
    def rolling_table ( self , n: int) -> dict :
        
        coordinates = self.getting_coordinates( self.table( f"""Table{n}""") )
        return {"data": self.accumulating_data( coordinates ), "coordinates": self.elaborating_coordinates(coordinates)}



if __name__ == '__main__' :
    # wb = load_workbook( 'trial.xlsx' )
    # ws = wb.active
    a = excel( 'trial.xlsx')
    print( a.rolling_table(1))
    c = 0