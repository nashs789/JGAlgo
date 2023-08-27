import sys
input = sys.stdin.readline

A = [0] + list(input().rstrip())
#print(A)
B = [0] + list(input().rstrip())
#print(B)
c = [[""]*len(B) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            c[i][j] = c[i-1][j-1] + A[i]
        else:
            if len(c[i-1][j]) >= len(c[i][j-1]):
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]

result = c[-1][-1]
