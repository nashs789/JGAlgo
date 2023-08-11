import sys

N = int(sys.stdin.readline())
cnt = 0

if N < 100:
    print(N)
    sys.exit()

for item in range(101, N+1):
    a = int(item / 100)
    b = int(item % 100 / 10)
    c = int(item % 100 % 10)

    if a - b == b - c:
        cnt += 1
    
print(cnt + 99)