import sys
N = int(sys.stdin.readline())
paper=[]
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
b_counter = 0
w_counter = 0

def paper_cutter(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                paper_cutter(x, y, N//2)
                paper_cutter(x, y + N//2, N//2)
                paper_cutter(x + N//2, y, N//2)
                paper_cutter(x + N//2, y + N//2, N//2)
                return
    if color == 0:
        global w_counter
        w_counter += 1
    else:
        global b_counter
        b_counter += 1

paper_cutter(0, 0, N)        

print(w_counter)
print(b_counter)
