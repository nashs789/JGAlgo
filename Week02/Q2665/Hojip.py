import sys
import heapq

n= int(sys.stdin.readline())

givenMiro = [list(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(len(givenMiro)) :
    givenMiro[i] = list(map(int, givenMiro[i]))

start = [0]

def move(x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = []
    heapq.heappush(q, [0, x, y])
    while q:
        c, y1, x1 = heapq.heappop(q)
        visited[y1][x1] = True

        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=y1+dy<=n-1 and 0<=x1+dx<=n-1 and not visited[y1+dy][x1+dx]:
                if givenMiro[y1+dy][x1+dx]:
                    cost = c
                else:
                    cost = c+1
                
                visited[y1+dy][x1+dx] = True
                heapq.heappush(q, [cost, y1+dy, x1+dx])
                if y1+dy == n-1 and x1+dx == n-1:
                    print(cost)
                    return

move(0, 0)