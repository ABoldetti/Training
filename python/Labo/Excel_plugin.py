from openpyxl import load_workbook
from openpyxl.worksheet.table import Table
import numpy as np



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
    
    def accumulating_data ( self , a :dict ) -> np.array :

        c = 0
        
    def rolling_table ( self ):
        for n in range( len( self.ws.tables.values() ) ) :
            coordinates = self.table( f"""Table{n}""")
            ausy = np.array()
            ausy = self.accumulating_data( coordinates )



if __name__ == '__main__' :
    wb = load_workbook( '/Users/andreaboldetti/Documents/GitHub/My_first_Repository/trial.xlsx' )
    ws = wb.active
    print( len(ws.tables.values()))