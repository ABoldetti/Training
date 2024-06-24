from numpy import array, inf

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
