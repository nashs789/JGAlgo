import sys
N = int(sys.stdin.readline())
matrix = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    print(row)
    matrix.append(row)
print(matrix)