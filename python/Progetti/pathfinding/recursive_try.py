from numpy import ones, array, inf, arange
from utilities import *
'''
TODO 
nel for usare come condizione una funzione che controlla se tutti quelli circostanti siano non inf
fare un'altra funzione che rileva gli inf residui e gli dà il valore minimo vicino, loopare finchè tutti gli inf non se ne sono andati
'''



def step(coord, i):
    if i == 0:
        coord[0]+=1
        pass
    elif i == 1:
        coord[0]-=1
        pass
    elif i == 2:
        coord[1]+=1
        pass
    elif i == 3:
        coord[1]-=1
        pass
    return coord
def case_check( map , x , y ):
    for i in range(4):
        temp = step( [x,y] , i )
        if temp[0] >= 0 and temp[0]<len(map) and temp[1] >= 0 and temp[1]<len(map):
            if map[temp[0] , temp[1]] != inf:
                return True
    return False
def start( map , i , j):
    a = i 
    b = j
    cristoddio = 0
    temp = [0,0]
    counter = 0
    while case_check(map , a,b):
        for k in range(4):
            #print('\t\t\t\t' , temp[0],temp[1] , '\t\t' , a,b)
            temp = step([a,b] , k)
            # print(temp)
            if temp[0] >= 0 and temp[0]<len(map) and temp[1] >= 0 and temp[1]<len(map):
                print('-------------------------------------CHECK 3--------------------------------------------')
                print(map, '\t\t' , temp[0],temp[1] , '\t\t' , a,b)
                if map[temp[0],temp[1]] > map[a,b]+1:
                    cristoddio+=1
                    map[temp[0],temp[1]] = map[a,b]+1
        for j in range(4):
            # Il problema è qua
            temp = step([a,b] , j)
            print('-------------------------------------CHECK 4--------------------------------------------')
            print(map, '\t\t' , temp[0],temp[1] , '\t\t' , a,b  , '\t\t' , temp[0] >= 0 and temp[0]<len(map) and temp[1] >= 0 , temp[1] >0 and temp[1]<len(map))
            if temp[0] >=0 and temp[0]<len(map) and temp[1] >=0 and temp[1]<len(map):
                print( '---------------------------------------BAZINGA---------------------------------------------')
                if map[temp[0],temp[1]]!=-1 and map[temp[0],temp[1]]> map[ a , b ]+1:
                    a = temp[0]
                    b = temp[1]
                    print( a , b)
                break
        counter+=1
    return map,cristoddio
def find_path(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i,j] == 0:
                map,cristoddio = start(map ,i,j)
    print(cristoddio)
    return map


if __name__ == '__main__':
    #print(find_path(maze))
    print( case_check(maze , 0 , 0))
