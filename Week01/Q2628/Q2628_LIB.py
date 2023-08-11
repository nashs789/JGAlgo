import sys

w, h = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
row = []
col = []

for _ in range(cnt):
    Type, pos = map(int, sys.stdin.readline().split())
    
    if Type == 0:
        row.append(pos)
    else:
        col.append(pos)

row.append(h)
col.append(w)
row = sorted(row)
col = sorted(col)

curX = 0
curY = 0
maxV = 0

for r in row:
    for c in col:
        square = abs(r - curY) * abs(c - curX)
        maxV = max(square, maxV)
        curX = c
    curX = 0
    curY = r

print(maxV)