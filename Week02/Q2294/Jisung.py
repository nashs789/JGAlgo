import sys
from collections import deque

input = sys.stdin.readline

n,k=map(int,input().split())
result = sys.maxsize

coin = [int(input()) for _ in range(n)]

def bfs(x,cnt):
    q = deque()
    q.append((x,0))
    while q:
        new,cnt = q.popleft()
        cnt += 1
        if new==k:
            return cnt
        
        for i in coin:
            if new + i < k:
                q.append((new+i,cnt))

for i in coin:
    result = min(result, bfs(i,0))
print(result)
        