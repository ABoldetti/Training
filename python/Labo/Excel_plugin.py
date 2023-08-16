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
        a = self.getting_coordinates( coordinates )
        ausy = list()
        df = pd.DataFrame(ausy)
        
        for i in range( ord( a [ 0 ] ) , ord( a [ 2 ] ) ):
            ausy = list()
            for j in range( a [ 1 ] + 1 , a [ 3 ]+1 ):
                ausy.append( (self.ws[f"""{chr(i)}{j}"""].value) )
            df[ str(self.ws[f"""{chr(i)}{a[1]}"""].value) ] = pd.DataFrame(ausy)
        print(df)

    def getting_coordinates ( self , set :dict ) -> dict :
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
        
        coordinates = self.table( f"""Table{n}""")
        ausy = np.array()
        return {"data": self.accumulating_data( coordinates ), "coordinates": self.elaborating_coordinates(coordinates)}



if __name__ == '__main__' :
    wb = load_workbook( 'trial.xlsx' )
    ws = wb.active
    print( ws.tables.values())
    #a = excel( 'trial.xlsx')
    #a.accumulating_data( ['D4', 'H13'])