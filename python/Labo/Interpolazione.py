import numpy as np

#in output viene ritornata un dizionario contenente in ordine (A, sA, B, sB)
#pane fuori
class interpolazione:
    def __init__(self, x: np.array, y: np.array, sY):
        self.x = x
        self.y = y
        self.sY = sY
        if type( self.sY ) is float or type( self.sY ) is int:
            self.a = True
        else: 
            self.a = False
        pass
    def Lineare( self ) -> dict:
        if np.size( self.x ) != np.size( self.y ) :
            print("Dati inseriti non validi")
        else:
            delta = np.size( self.x ) * np.sum( np.power( self.x , 2 ) )- np.power( np.sum( self.x ), 2 )
            B = ( np.sum( self.y ) * np.sum( np.power( self.x , 2 ) ) - np.sum( self.x ) * np.sum( self.x * self.y ) ) / delta
            A = ( np.size( self.x ) * np.sum( self.x * self.y ) - np.sum( self.x ) * np.sum( self.y ) ) / delta
            sB = ( np.sqrt( np.sum( np.power(self.x , 2) )/ delta)) * self.sY
            sA = ( np.sqrt( np.size( self.x ) / delta) ) * self.sY
            return {"A value" : A, "A error": sA, "B value": B, "B error": sB}
    def LinOrigine(self) -> dict:
            if np.size( self.x ) != np.size( self.y ) :
                print("Dati inseriti non validi")
            else:
                A = np.sum( self.x * self.y ) / np.sum( np.power(self.x , 2) )
                sA = self.sY / np.sqrt( np.sum( np.power(self.x , 2) ))
                return {"A value": A, "A error": sA}
    def Pesata(self) -> dict:
        delta = np.sum( 1 / np.power( self.sY , 2 ) ) * np.sum( np.power( self.x / self.sY , 2 )) - np.power( ( np.sum( self.x / np.power( self.sY , 2)) ) , 2)
        B = ( np.sum( self.y / np.power(self.sY , 2) ) * np.sum( np.power( ( self.x / self.sY ) , 2 ) ) - np.sum( self.x / np.power(self.sY , 2)) * np.sum( self.x * self.y / np.power( self.sY , 2)) )/ delta
        A = ( np.sum( 1 / np.power(self.sY , 2) ) * np.sum( self.x * self.y / np.power( self.sY , 2 ) ) - np.sum( self.x / np.power( self.sY , 2 ) ) * np.sum( self.y / np.power( self.sY , 2 ))) / delta
        sB = np.sqrt( np.sum( np.power( ( self.x / self.sY ) , 2 ) ) / delta )
        sA = np.sqrt( np.sum( 1 / np.power( self.sY , 2 ) ) / delta )
        sAB = np.sqrt( np.sum( self.x / np.power( self.sY ,2 ) ) / delta )
        return {"A value" : A, "A error" : sA, "B value": B, "B error": sB, "covariant": sAB}
    def Selezione(self) ->dict:
        if self.a :
            if int ( input("inserire 1 per intersezione nell'origine, 0 per nessun vincolo\t") ):
               return self.LinOrigine()
            else:
               return self.Lineare()
        else:
            return self.Pesata()


if __name__ == '__main__':
    x=np.array([1,2,3,4,5,6])
    y=np.array([0.1,0.2,0.3,0.4,0.5,0.6])
    sy=np.array([0.1,0.3,0.2,0.1,0.2,0.3])
    #sy=0.1
    a=interpolazione(x,y,sy)
    print(a.Selezione())
    