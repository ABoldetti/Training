from numpy import zeros

'''
colour = True --> black
colour = False --> white
side = True --> left
side = False --> right
pos = ( x , y) = ( column , row ) = ( Letter , Number)
'''


class Board:

        
    def __init__(self , std) -> None:
        if std:
            self.white = side( False )
            self.black = side( True )
        else: 
            self.white = edit( False )
            self.black = edit( True )
        pass

    


# colour True is black, False is white
class King:
    def __init__(self,colour,pos = 0) -> None:
        self.colour = colour
        self.move = False
        if pos == 0:
            if self.colour:
                self.pos = ( 7 , 4 )
            else:
                self.pos = ( 0 , 4 )
        else: self.pos = pos
        pass

    def move ( self , a: tuple ):
        for i,j in zip(a,self.pos):
            if abs(i-j) >1:
                print( ValueError , 'move is uncompatible')
                return 0
            else: 
                self.pos = a
                return 1
# colour True is black, False is white
class Queen:
    def __init__(self,colour,pos = 0) -> None:
        self.colour = colour
        self.move = False
        if pos == 0:
            if self.colour:
                self.pos = ( 7 , 3 )
            else:
                self.pos = ( 0 , 3 )
        else: self.pos = pos
        pass
    def move ( self , a: tuple ):
        if self.move[0] == a[0] or self.move[1] == a[1] or abs(a[0]-self.pos[0]) == abs(a[1]-self.pos[1]):
            self.pos = a
            return 1
        else: 
            print( ValueError , 'move is uncompatible')
            return 0
    
# colour True is black, False is white
# side True is left, False is right
class Bishop:
    def __init__(self, colour , side , pos = 0) -> None:
        self.colour = colour
        if pos == 0:
            self.colour = colour
            if self.colour == False:
                a = 0
            else:
                a = 7
            
            if side == True:
                b = 2
            else:
                b = 5
            
            self.pos = ( a , b)
        
        else: self.pos = pos
        pass

    def move ( self , a: tuple ):
        if abs(a[0]-self.pos[0]) == abs(a[1]-self.pos[1]):
            self.pos = a
            return 1
        else:
            print( ValueError , 'move is uncompatible')
            return 0

class Rook:
    def __init__(self , colour , side , pos = 0) -> None:
        self.move = False
        self.colour = colour
        if pos == 0:
            self.colour = colour
            if self.colour == False:
                a = 0
            else:
                a = 7
            
            if side == True:
                b = 0
            else:
                b = 7
            
            self.pos = ( a , b)
        
        else: self.pos = pos
        pass

    def move( self , a: tuple):
        if a[0] == self.pos[0] or a[0] == self.pos[0]:
            self.pos = a
            return 1
        else:
            print( ValueError , 'move is uncompatible')
            return 0
        
class Knight:
    def __init__(self , colour , side , pos = 0) -> None:
        if pos == 0:
            self.colour = colour
            if self.colour == False:
                a = 0
            else:
                a = 7
            
            if side == True:
                b = 1
            else:
                b = 6
            
            self.pos = ( a , b)
        
        else: self.pos = pos
        pass

    def move ( self , a: tuple):
        sum = 0
        for i,j in zip( self.pos , a):
            shift = abs(i-j)
            if shift == 3:
                print( ValueError , 'move uncompatible')
                return 0
            sum+= shift
        if sum == 3: self.pos = a
        else:
            print( ValueError , 'move uncompatible')
            return 0
        
class Pawn:
    def __init__(self, colour , pos ) -> None:
        self.colour = colour
        if type(pos) == tuple:
            self.pos = pos
        elif type(pos) == int:
            if colour:
                self.pos = ( 6 , pos)
            else:
                self.pos = ( 1 , pos)
        if colour and pos[1] == 7:
            print( ValueError , 'a pawn cannot stay on the first row')
            self.pos = 0
        if not colour and pos[1] == 0:
            print( ValueError , 'a pawn cannot stay on the first row')
            self.pos = 0
        pass

    def move( self , a):
        if self.colour:
            if a[1] - self.pos[1] < 0 and a[0] == self.pos[0]:
                self.pos = a
                return 1
            elif Board.piece( self.pos , a) and abs(a[0]-self.pos[0]) == a[1]-self.pos[1]:
                self.pos = a
                return 1
            else:
                print( ValueError , 'move is uncompatible')
                return 0




def freespace( pos1 , pos2 ):

    pass

def check( pos ):

    pass

# TDL check if every square is not through check
def castle( King , Rook):
    if King.move and Rook.move and freespace(King.pos,Rook.pos) and check(King.pos):
        if King.pos[1] > Rook.pos[1]:
            King.pos[1] = 2
            Rook.pos[1] = 3

        else:
            King.pos[1] = 6
            Rook.pos[1] = 5
        return 1
    else:
        print( ValueError , 'move uncompatible')
        return 0

def side( colour: bool ) -> dict:
    K = King( colour )
    Q = Queen( colour )
    B1 = Bishop( colour , False )
    B2 = Bishop( colour , True )
    N1 = Knight( colour , False )
    N2 = Knight( colour , True )
    R1 = Rook( colour , False )
    R2 = Rook( colour , True )
    pawn = {}
    for i in range( 8 ):
        pawn[f'p{i+1}'] = Pawn( colour , i)
    if colour:
        return { 'bK': K , 'bQ' : Q , 'bB1' : B1 , 'bB2' : B2 , 'bN1' : N1 , 'bN2' : N2 , 'bR1' : R1 , 'bR2' : R2 , 'wpawns':pawn}
    else:
        return { 'wK': K , 'wQ' : Q , 'wB1' : B1 , 'wB2' : B2 , 'wN1' : N1 , 'wN2' : N2 , 'wR1' : R1 , 'wR2' : R2 , 'wpawns':pawn}
    
def edit( colour ):
    pass