import sys
from collections import deque

input = sys.stdin.readline

n,k=map(int,input().split())
coins = [int(input()) for _ in range(n)]
check = [0 for _ in range(100001)]

def bfs():
    q = deque()
    for coin in coins:
        cnt = 1
        q.append((coin,cnt))
        check[coin] = 1
    while q:
        new,cnt = q.popleft()
        if new==k:
            return cnt
        for i in coins:
            sums = new + i
            if sums > k:
                continue
            elif check[sums]==0:
                check[sums] = 1
                q.append((sums,cnt+1))
    return -1
    
print(bfs())