import sys
n, k = map(int, sys.stdin.readline().split())
levels = [int(sys.stdin.readline()) for _ in range(n)]

start = min(levels)
end = start + k

res = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0

    for level in levels:
        if mid > level:
           sum+= (mid - level)
    if sum <= k:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1

print(res)