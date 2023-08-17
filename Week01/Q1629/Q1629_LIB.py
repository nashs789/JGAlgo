import sys

A, B, C = map(int, sys.stdin.readline().split())

def func(a, b):
    if b == 1:
        return a % C
    else:
        calc = func(a, b//2)

        if b % 2 == 1:
            return (calc * calc * a) % C
        else:
            return (calc * calc) % C

print(func(A, B))