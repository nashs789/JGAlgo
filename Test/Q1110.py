import sys

N = int(sys.stdin.readline().strip('\n'))

A = N / 10
B = int(N % 10)
C = A + B
idx = 0

while True:
    A, B = int(B % 10), int(C % 10)
    C = A + B
    idx += 1
    
    if int(str(A) + str(B)) == int(N):
        print(idx)
        break