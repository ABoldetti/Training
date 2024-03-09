class king:
    def __init__(self,colour,pos = (7,4) if colour else (0,4)) -> None:
        self.colour = colour
        self.move = False
        if self.colour == False:
            self.pos = ( 0 , 4 )
        else:
            self.pos = ( 7 , 4 )
        pass

    def move ( self , a ):
        for i,j in zip(a,self.pos):
            if abs(i-j) >1:
                print( TypeError , 'move is uncompatible')
                return 0
            else: return 1

class bishop:
    def __init__(self, colour , side) -> None:
        self.colour = colour
        if self.colour == False:
            if side == True:
                self.pos = ( 0 , 4 )
        else:
            self.pos = ( 7 , 4 )
        pass

    def move ( self , a ):
        for i,j in zip(a,self.pos):
            if abs(i-j) >1:
                print( TypeError , 'move is uncompatible')
                return 0
            else: return 1

