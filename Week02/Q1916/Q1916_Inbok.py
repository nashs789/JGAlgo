import sys
import heapq

def dijkstra(srt):
    pQueue = [(srt, 0)]
    dist[srt] = 0

    while pQueue:
        cur_node, cur_dist = heapq.heappop(pQueue)

        if dist[cur_node] < cur_dist:
            continue

        for linked_node, cost in adj[cur_node]:
            next_dist = dist[cur_node] + cost

            if dist[linked_node] > next_dist:
                heapq.heappush(pQueue, (linked_node, next_dist))
                dist[linked_node] = next_dist

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    adj = [[] for _ in range(N + 1)]
    dist = [sys.maxsize] * (N + 1)

    for _ in range(M):
        srt, end, cost = map(int, sys.stdin.readline().split())
        
        adj[srt].append((end, cost))

    srt, end = map(int, sys.stdin.readline().split())
    dijkstra(srt)
    print(dist[end])