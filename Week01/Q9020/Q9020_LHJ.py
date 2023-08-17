import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

count = int(sys.stdin.readline())
for _ in range(count):
    num = int(sys.stdin.readline())
    mid = num//2

    while mid > 0:
        if isPrime(mid):
            if isPrime(num-mid):
                print(mid, num-mid)
                break
        mid-=1
