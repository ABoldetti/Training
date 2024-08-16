from numpy import inf
from utilities import *

#//def trial( a, b):
#//    return a+b




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
            return abs( coord_tmp[0] - i)
    return abs( coord_tmp[0] - i)
            
def dist_Y(map, coord_sor, coord_tmp):
    i = 0
    for i in arange( coord_tmp[1] , coord_sor[1]):
        if map[coord_tmp[0] , i] == -1:
            return abs( coord_tmp[1] - i+1)
    return abs( coord_tmp[1] - coord_sor[0]+1)

def dist( map , coordp , coord_sor):
    coord_tmp = list(coordp)
    dist = 0
    ausy = [coord_tmp]
    list_dist = []
    #^----------------------------------------------------------------------------------------------------------------------
    while coord_tmp != list(coord_sor):
        rel_d = dist_X(map, coord_sor, coord_tmp)

        dist += rel_d
        coord_tmp[0] = coord_tmp[0] + rel_d if coord_tmp[0] < coord_sor[0] else coord_tmp[0] - rel_d
        # Update the x-coordinate of coord_tmp based on the relative distance rel_d
        # If coord_tmp[0] is less than coord_sor[0], add rel_d to coord_tmp[0], otherwise subtract rel_d from coord_tmp[0]


        rel_d = dist_Y(map, coord_sor, coord_tmp)
        
        dist += rel_d
        coord_tmp[1] = coord_tmp[1] + rel_d if coord_tmp[1] < coord_sor[1] else coord_tmp[1] - rel_d
        # Update the y-coordinate of coord_tmp based on the relative distance rel_d
        # If coord_tmp[1] is less than coord_sor[1], add rel_d to coord_tmp[1], otherwise subtract rel_d from coord_tmp[1]


        if len(ausy) > 2: ausy.pop(0)
        ausy.append(coord_tmp)
        if ausy[-1] == ausy[-2]:
            break
        # Check if the last two elements in ausy are the same
        # If they are the same, it means that coord_tmp is not changing anymore and we can break out of the loop

    if coord_tmp == list(coord_sor):
        # If coord_tmp is equal to coord_sor, it means we have reached the source coordinate
        return dist
        # Return the total distance traveled

    list_dist.append(dist)
    dist = 0

    #^----------------------------------------------------------------------------------------------------------------------
    while coord_tmp != list(coord_sor):
        rel_d = dist_Y(map, coord_sor, coord_tmp)
        
        dist += rel_d
        
        coord_tmp[1] = coord_tmp[1] + rel_d if coord_tmp[1] < coord_sor[1] else coord_tmp[1] - rel_d
        
        # Update the y-coordinate of coord_tmp based on the relative distance rel_d
        # If coord_tmp[1] is less than coord_sor[1], add rel_d to coord_tmp[1], otherwise subtract rel_d from coord_tmp[1]

        rel_d = dist_X(map, coord_sor, coord_tmp)

        dist += rel_d
        
        
        coord_tmp[0] = coord_tmp[0] + rel_d if coord_tmp[0] < coord_sor[0] else coord_tmp[0] - rel_d
        
        # Update the x-coordinate of coord_tmp based on the relative distance rel_d
        # If coord_tmp[0] is less than coord_sor[0], add rel_d to coord_tmp[0], otherwise subtract rel_d from coord_tmp[0]

        if len(ausy) > 2: ausy.pop(0)
        ausy.append(coord_tmp)
        if ausy[-1] == ausy[-2]:
            break
        # Check if the last two elements in ausy are the same
        # If they are the same, it means that coord_tmp is not changing anymore and we can break out of the loop
    
    if coord_tmp == list(coord_sor):
        # If coord_tmp is equal to coord_sor, it means we have reached the source coordinate
        return dist
        # Return the total distance traveled

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

