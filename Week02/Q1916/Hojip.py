import sys
import heapq
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

distance = [math.inf] * (N+1)

graph= [[]for _ in range(N+1)]

for _ in range(M) :
    A, B, C = map(int,sys.stdin.readline().split())
    graph[A].append((B, C))

start, end = map(int,sys.stdin.readline().split())

def dijkstra(start) :
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap :
        #최단거리가 짧은 노드에대한 정보 꺼내기
        dist, now = heapq.heappop(heap)
        #이미 처리된 노드 였으면 무시(최단거리와 비교를 통해 방문여부 확인)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
                
dijkstra(start)

print(distance)