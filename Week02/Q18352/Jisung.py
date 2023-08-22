import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X=map(int,input().split())
graph = [[] for _ in range(N+1)]
is_minway = [0] * (N+1)
visited = [False] *(N+1)

for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)

# X로 시작해서 K번째를 print해준다.
def bfs(v):
    answer = []
    q = deque([v])
    visited[v] = True
    is_minway[v] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                is_minway[i] = is_minway[now] + 1
                if is_minway[i]==K:
                    answer.append(i)
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(X)
# 내 풀이 
# 1. X로 시작해서 K번 마다 print를 해주는데 K번을 세는방법이 잘못되었음

# 보고푼 풀이
# 1. X로 시작해서 K번 마다 print는 맞지만 더해주는 방식이 다르다.
# 2. 해당 숫자가 그 전에 숫자에 의해서 불려질때마다 전숫자에서 +1해주는 방식으로 커진다.