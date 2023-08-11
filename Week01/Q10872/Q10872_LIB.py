import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

num = int(sys.stdin.readline())

if num == 0:
    print(1)
else:
    print(factorial(num))