import sys
from collections import deque

M, N, H = map(int,sys.stdin.readline().split()) # X, Y, Z순으로 받아옴

givenTomato = [[[int(k) for k in sys.stdin.readline().split()] for _ in range(N)] for _ in range(H)]


q = deque()
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if givenTomato[i][j][k] == 1 : # 완숙토마토들을 전부 q에 append
                q.append((i, j, k))

d = [[0,0,1], [0,0,-1], [1,0,0], [-1,0,0], [0,1,0], [0,-1,0]]

def BFS() :
    while q :
        z, x, y = q.popleft()
        for dz, dx, dy in d :
            if 0<= dz+z < H and 0<= dx+x < N and 0<= dy+y < M :
                if givenTomato[dz+z][dx+x][dy+y] == 0 :
                    givenTomato[dz+z][dx+x][dy+y] = givenTomato[z][x][y] + 1
                    q.append((dz+z, dx+x, dy+y))

BFS()

flag = False
max_value = 0
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if givenTomato[i][j][k] == 0:
                flag = True
            max_value = max(max_value, givenTomato[i][j][k])

if flag :
    print(-1)
else :
    print(max_value -1) # 첫날부터 시작하기때문에 -1