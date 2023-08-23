import sys
from collections import deque
R, C = map(int,sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

visited = [[False for _ in range(C)]for _ in range(R)]

d = [[1, 0],[-1, 0], [0, 1], [0, -1]]


def flood() :
    water = []
    for i in range(R) :
        for j in range(C) :
            if graph[i][j] == '*' :
                for dx, dy in d :
                    if 0 <= i+dx < R and 0 <= j+dy < C and graph[i+dx][j+dy] == '.':
                        water.append((i+dx, j+dy))
                
    for x,y in water :
        graph[x][y] = '*'

def BFS(x, y) :
    q = deque([(x, y)])
    
    visited[x][y] = True
    cnt = 0
    
    while q : 
        cnt += 1
        flood()
        length = len(q)
        for _ in range(length) :
            x, y = q.popleft()
            for dx, dy in d :
                if 0 <= dx+x < R and 0 <= dy+y < C and not visited[dx+x][dy+y] :
                    if graph[dx+x][dy+y] == '.' :
                        q.append((dx+x, dy+y))
                        visited[dx+x][dy+y] = True
                    elif graph[dx+x][dy+y] == 'D' :
                        return cnt
    return 'KAKTUS'

sx , sy = 0, 0
for i in range(R) :
    for j in range(C) :
        if graph[i][j] == 'S' :
            sx, sy = i, j
            
print(BFS(sx, sy))