import sys
import math

def is_prime(n):
    if n == 1:
        return False

    sqrt = int(math.sqrt(n)) + 1
    for idx in range(2, sqrt):
        if n % idx == 0:
            return False

    return True

cnt = sys.stdin.readline()
List = map(int, sys.stdin.readline().split())

print(len(list(filter(is_prime, List))))