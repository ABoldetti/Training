from numpy import ones, array, inf
from utilities import *

def arange( start , end = None , step = 1):
    if end == None:
        end = start
        start = 0
    pos = 0
    l = []
    while pos < abs(start - end):
        l.append( int(start + abs(end-start)/(end-start)*pos))
        pos+=step
    return l

def find_start( map ):
    source = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i,j] == 0:
                source.append((i,j))
    return source

def check( map ):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i,j] == inf: return False
    return True

def dist_X(map, coord_sor, coord_tmp):
    i = 0
    for i in arange( coord_tmp[0] , coord_sor[0]):
        if map[i,coord_tmp[1]] == -1:
            return abs( coord_tmp[0] - i+1)
    return abs( coord_tmp[0] - i+1)
            
def dist_Y(map, coord_sor, coord_tmp):
    i = 0
    for i in arange( coord_tmp[1] , coord_sor[1]):
        if map[coord_tmp[0] , i] == -1:
            return abs( coord_tmp[1] - i+1)
    return abs( coord_tmp[1] - i+1)

def dist( map , coordp , coord_sor):
    coord_tmp = list(coordp)
    dist = 0
    ausy = [coord_tmp]
    list_dist = []


    while coord_tmp != coord_sor:
        rel_d = dist_X(map, coord_sor, coord_tmp)

        dist += rel_d
        coord_tmp[0] = coord_tmp[0] + rel_d if coord_tmp[0] < coord_sor[0] else coord_tmp[0] - rel_d
        #print( '-----------------------------------', coord_tmp , coord_sor, '-------------------------------------')

        rel_d = dist_Y(map, coord_sor, coord_tmp)
        
        dist += rel_d
        coord_tmp[1] = coord_tmp[1] + rel_d if coord_tmp[1] < coord_sor[1] else coord_tmp[1] - rel_d
        #print( '-----------------------------------', coord_tmp , coord_sor, '-------------------------------------')

        if len(ausy) > 2: ausy.pop( 0 )
        ausy.append( coord_tmp )
        if ausy[-1] == ausy[-2]:
            break
    if coord_tmp == coord_sor:
        #print( '-----------------------------------' , dist , '-------------------------------------', coord_tmp , coord_sor, '-------------------------------------')
        return dist
    list_dist.append(dist)
    dist = 0

    

    while coord_tmp != coord_sor:
        rel_d = dist_Y(map, coord_sor, coord_tmp)
        
        dist += rel_d
        coord_tmp[1] = coord_tmp[1] + rel_d if coord_tmp[1] < coord_sor[1] else coord_tmp[1] - rel_d
        #print( '-----------------------------------', coord_tmp , coord_sor, '-------------------------------------')

        rel_d = dist_X(map, coord_sor, coord_tmp)

        dist += rel_d
        coord_tmp[0] = coord_tmp[0] + rel_d if coord_tmp[0] < coord_sor[0] else coord_tmp[0] - rel_d
        #print( '-----------------------------------', coord_tmp , coord_sor, '-------------------------------------')

        if len(ausy) > 2: ausy.pop( 0 )
        ausy.append( coord_tmp )
        if ausy[-1] == ausy[-2]:
            break
    
    if coord_tmp == coord_sor:
        #print( '-----------------------------------' , dist , '-------------------------------------', coord_tmp , coord_sor, '-------------------------------------')
        return dist
    list_dist.append(dist)
    dist = 0

def pathfind( map ):
    source = find_start(map)
    if len( source ) == 1: source = tuple(source[0])
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i,j] = dist(map , (i,j) , source )

    if not check(map): print('FAILED')
    return map




    


    
    







if __name__ == '__main__':
    print( dist_X( map , (1,1) , (0,0)))
    #print(maze)
    print( pathfind( maze ))

