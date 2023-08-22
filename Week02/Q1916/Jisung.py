import sys
import heapq as hq
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
M = int(input())
visited = [False] * (N+1)
distance = [inf] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M+2):
    s,e,c = map(int,input().split())
    graph[s].append([e,c])

start,end = map(int,input().split())

def Dijkstra(s):
    q = []
    hq.heappush(q,(c, s))
    while q:
        cost, now = hq.heappop(q)
        for t,v in graph[now]:
            new_cost = cost + v
            if distance[t]>new_cost:
                distance[t] = new_cost
                hq.heappush(q,(new_cost,t))
Dijkstra(start)
print(distance[end])