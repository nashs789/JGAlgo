# import sys
# from heapq import heappop, heappush

# def dijkstra(srt):
#     queue = [(0, 0, srt)] 

#     while queue:
#         order, cur_time, cur_node = heappop(queue)

#         if times[cur_node] > cur_time:
#             continue
        
#         for order, spend_time, linked_node in adj[cur_node]:
#             new_time = times[cur_node] + spend_time

#             if times[linked_node] < new_time:
#                 times[linked_node] = new_time
#                 heappush(queue, (-new_time, new_time, linked_node))

#             print(times)
#             print(times[linked_node], new_time)
#             print(node_path)
#             if times[linked_node] < new_time:
#                 times[linked_node] = new_time
#                 node_path[linked_node].clear()
#             elif times[linked_node] == new_time:
#                 node_path[linked_node].append(cur_node)

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     m = int(input())
#     times = [0 for _ in range(n + 1)]
#     node_path = [[] for _ in range(n + 1)]       # 노드 까지 최고로 걸리는 시간에 해당하는 경로 리스트 (시간 갱신할 때 같이 갱신됨) 
#     adj = [[] for _ in range(n + 1)]

#     for _ in range(m):
#         srt, end, time = map(int, input().split())
#         adj[srt].append((-time, time, end))

#     srt, end = map(int, input().split())

#     dijkstra(srt)
#     path = set()
#     queue = [end]

#     while queue:
#         cur_node = heappop(queue)

#         for node in node_path[cur_node]:
#             if (node, cur_node) not in path:
#                 heappush(queue, node)
#                 path.add((node, cur_node))

#     print(times[end])
#     print(len(path))

# import sys
# from collections import deque

# def topology_sort():
#     while queue:
#         cur_node = queue.popleft()

#         for spend_time, linked_node in adj[cur_node]:
#             in_degree[linked_node] -= 1

#             if times[linked_node] < times[cur_node] + spend_time:
#                 times[linked_node] = times[cur_node] + spend_time
#                 node_path[linked_node] = [cur_node]
#             elif times[linked_node] == times[cur_node] + spend_time:
#                 node_path[linked_node].append(cur_node)

#             if in_degree[linked_node] == 0:
#                 queue.append(linked_node)


# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     m = int(input())
#     times = [0 for _ in range(n + 1)]
#     in_degree = [0 for _ in range(n + 1)]
#     adj = [[] for _ in range(n + 1)]
#     node_path = [[] for _ in range(n + 1)]
#     queue = deque()

#     for _ in range(m):
#         srt, end, time = map(int, input().split())
#         adj[srt].append((time, end))
#         in_degree[end] += 1

#     srt, end = map(int, input().split())
#     queue.append(srt)

#     topology_sort()

#     queue = deque([end])
#     path = set()
#     while queue:
#         cur_node = queue.popleft()

#         for node in node_path[cur_node]:
#             if (cur_node, node) not in path:
#                 path.add((cur_node, node))
#                 queue.append(node)

#     print(times[end])
#     print(len(path))

# import sys
# from heapq import heappop, heappush

# def topology_sort():
#     while queue:
#         cur_time, cur_node = heappop(queue)

#         for time, linked_node in adj[cur_node]:
#             in_degree[linked_node] -= 1
#             new_time = cur_time + time

#             if new_time > times[linked_node]:
#                 times[linked_node] = new_time
        
#             if in_degree[linked_node] == 0:
#                 heappush(queue, (new_time, linked_node))

#             if node_max_time[linked_node] < new_time:    
#                 node_max_time[linked_node] = new_time
#                 node_path[linked_node] = [cur_node]
#             elif node_max_time[linked_node] == new_time:
#                 node_path[linked_node].append(cur_node)

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n = int(input())
#     m = int(input())
#     times = [0 for _ in range(n + 1)]
#     in_degree = [0 for _ in range(n + 1)]
#     adj = [[] for _ in range(n + 1)]
#     node_path = [[] for _ in range(n + 1)]       # 노드 까지 최고로 걸리는 시간에 해당하는 경로 리스트 (시간 갱신할 때 같이 갱신됨) 
#     node_max_time = [0 for _ in range(n + 1)]    # 노드 까지 걸리는 시간중 가장 큰 시간
#     queue = []

#     for _ in range(m):
#         srt, end, time = map(int, input().split())
#         adj[srt].append((time, end))
#         in_degree[end] += 1

#     srt, end = map(int, input().split())
#     heappush(queue, (0, srt))

#     topology_sort()

#     path = set()
#     queue = [end]

#     while queue:
#         cur_node = heappop(queue)

#         for node in node_path[cur_node]:
#             heappush(queue, node)
#             path.add((node, cur_node))

#     print(times[end])
#     print(len(path))

import sys
from collections import deque

def topology_sort():
    while queue:
        cur_node = queue.popleft()

        for spend_time, linked_node in graph[cur_node]:
            in_degree[linked_node] -= 1

            if times[linked_node] <= times[cur_node] + spend_time:
                times[linked_node] = times[cur_node] + spend_time

            if in_degree[linked_node] == 0:
                queue.append(linked_node)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    times = [0 for _ in range(n + 1)]
    in_degree = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    back_graph = [[] for _ in range(n + 1)]
    queue = deque()

    for _ in range(m):
        srt, end, time = map(int, input().split())
        graph[srt].append((time, end))
        back_graph[end].append((time, srt))
        in_degree[end] += 1

    srt, end = map(int, input().split())
    queue.append(srt)

    topology_sort()

    queue = deque()
    queue.append((times[end], end))
    visited = [False] * (n + 1)
    answer = 0
    
    while queue:
        cur_time, cur_node = queue.popleft()

        for spned_time, linked_node in back_graph[cur_node]:
            if cur_time == times[linked_node] + spned_time:
                answer += 1         
                if not visited[linked_node]:
                    visited[linked_node] = True
                    queue.append((times[linked_node], linked_node))       

    print(times[end])
    print(answer)