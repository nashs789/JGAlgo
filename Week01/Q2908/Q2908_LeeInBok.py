import sys

A, B = sys.stdin.readline().split()
maxV = max(int("".join(reversed(A))), int("".join(reversed(B))))

print(maxV)