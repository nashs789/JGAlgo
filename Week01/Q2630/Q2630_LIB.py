import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
color = [0, 0]

def cut(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y + n//2, n//2)
                cut(x + n//2, y, n//2)
                cut(x + n//2, y + n//2, n//2)
                return
            
    if paper[x][y] == 0:
        color[0] += 1
    else:
        color[1] += 1

cut(0, 0, N)
print(color[0])
print(color[1])