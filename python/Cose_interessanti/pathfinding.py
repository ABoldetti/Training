from numpy import ones, array, inf



map = array([[inf, -1, inf, inf, inf, -1, inf, inf, inf, inf],
              [inf, 0, inf, -1, inf, -1, inf, -1, inf, inf],
              [inf, inf, inf, -1, inf, inf, inf, -1, inf, inf],
              [inf, -1, -1, -1, inf, -1, inf, -1, inf, inf],
              [inf, inf, inf, inf, inf, -1, inf, -1, inf, inf],
              [inf, -1, inf, -1, inf, -1, inf, -1, inf, inf],
              [inf, inf, inf, -1, inf, inf, inf, -1, inf, inf],
              [inf, -1, -1, -1, inf, -1, inf, -1, 0, inf],
              [inf, inf, inf, inf, inf, -1, inf, -1, inf, inf],
              [inf, inf, inf, inf, inf, -1, inf, inf, inf, inf]])

maze = array([[inf, inf, inf],
                  [inf, 0, inf],
                  [inf, -1, inf]])

cristoddio = 0

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


def start( map , i , j):
    a = i 
    b = j
    cristoddio = 0
    temp = [0,0]
    for counter in range(len(map)**2):
        for k in range(4):
            temp = step([a,b] , k)
            # print(temp)
            if temp[0] >0 and temp[0]<len(map) and temp[1] >0 and temp[1]<len(map):
                print('-------------------------------------CHECK 3--------------------------------------------')
                print(map, '\t\t' , temp[0],temp[1] , '\t\t' , a,b)
                if map[temp[0],temp[1]] > map[a,b]+1:
                    cristoddio+=1
                    map[temp[0],temp[1]] = map[a,b]+1
                    print('-------------------------------------CHECK 2--------------------------------------------')
                    print(map, '\t\t' , temp[0],temp[1] , '\t\t' , a,b)
        a = temp[0]
        b = temp[1]
    return map,cristoddio


def find_path(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i,j] == 0:
                map,cristoddio = start(map ,i,j)
    print(cristoddio)
    return map

if __name__ == '__main__':
    print(find_path(maze))
