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


def start( i , j ):
    a = i 
    b = j

    for k in range(4):
            temp = step([a,b] , k)
            if map[temp[0],temp[1]] != inf: 
                continue
            elif map[temp[0],temp[1]]>map[a,b]+1:
                map[temp[0],temp[1]] = map[a,b]+1
                start(a,b)
        

def find_path(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i,j] == 0:
                start(i,j)
    return map

if __name__ == '__main__':
    print(find_path(maze))
    
