import sys

def coordinate(N, r, c):
    if N == 0:
        return 0
    
    size = 2 ** (N - 1)
    step = size * size * ((r //size) * 2 + (c // size))
    return step + coordinate(N - 1, r % size, c % size)


            
N, r, c = map(int, sys.stdin.readline().split())

result = coordinate(N, r, c)
print(result)