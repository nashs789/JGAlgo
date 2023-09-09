import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int,input().split())
visited = [0 for _ in range(10000001)]

def bfs(start,end):
    q = deque()
    count = 0
    q.append((start,count))
    visited[start] = 1
    while q:
        here,cnt = q.popleft()
        if here==end:
            print(cnt)
            return
        for i in [here-1, here+1, here*2]:
            if i > end + here:
                continue
            if not visited[i]:
                q.append((i,cnt+1))
                visited[i] = 1
bfs(start,end)