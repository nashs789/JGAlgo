def set_queen(row):
    global result
    if row == N:
        result += 1
        return
    
    for col in range(N):
        if (not diagsA[ row+col ] and not diagsB[ row-col ] and not pos[col]):
            pos[ col ] = diagsA[ row+col ] = diagsB[ row-col]  = True
            set_queen(row+1)
            pos[ col ] = diagsA[ row+col ] = diagsB[ row-col ] = False

import sys
N = int(sys.stdin.readline())
result = 0
pos = [False] * N
diagsA = [False] * (2*N - 1)
diagsB = [False] * (2*N - 1)
set_queen(0)
print(result)