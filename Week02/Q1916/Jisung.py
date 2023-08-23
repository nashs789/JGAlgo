import sys
import heapq as hq
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
M = int(input())
distance = [inf] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))

start,end = map(int,input().split())

# BFS - dijkstra알고리즘
def Dijkstra(s):
    q = []
    hq.heappush(q,(0, s))
    distance[s]=0

    while q:
        cost, now = hq.heappop(q)

        if distance[now] < cost:
            continue

        for t,v in graph[now]:
            new_cost = cost + t

            if distance[v]>new_cost:
                hq.heappush(q,(new_cost,v))
                distance[v] = new_cost

# 시작할때 첫 자기자신은 비용을 0으로 한다.
# 그 후 while문을 돌면서 cost와 now를 꺼낸다.
# distance[now]를 꺼내서 현재 비용과 비교했을 대 현재 비용이 더 크다면 비교할 필요없이 다음 루프로 돌린다.
# 그 후 그래프에서 now에 해당하는 값들을(연결되는값)들을 다 불러와서
# 각각의 distance보다 cost에 해당 가중치를 넣은 값과 비교하였을 때 더 작다면 q에 푸시를 해준다.
# distance의 값을 new_cost로 바꿔준다.


Dijkstra(start)
print(distance[end])