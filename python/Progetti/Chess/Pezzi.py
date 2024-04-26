
# colour True is black, False is white
class king:
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

    def move ( self , a ):
        for i,j in zip(a,self.pos):
            if abs(i-j) >1:
                print( TypeError , 'move is uncompatible')
                return 0
            else: 
                self.pos = a
                return 1

# colour True is black, False is white
# side True is left, False is right
class bishop:
    def __init__(self, colour , side) -> None:
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
        pass

    def move ( self , a ):
        if abs(a[0]-self.pos[0]) == abs(a[1]-self.pos[1]):
            self.pos = a
            return 1
        else:
            print( TypeError , 'move is uncompatible')
            return 0


