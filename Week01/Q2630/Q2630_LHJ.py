import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

def cutPaper( x, y, N ):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+N):
        for k in range(y, y+N):
            if color != paper[i][k]:
                cutPaper( x, y, N//2)
                cutPaper( x, y+N//2, N//2)
                cutPaper( x+N//2, y, N//2)
                cutPaper( x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white +=1
    else:
        blue +=1

white = 0
blue = 0
cutPaper(0, 0, N)
print(white)
print(blue)