# import sys
# sys.setrecursionlimit(10 ** 7)

# answer = 0

# def dfs(node, dist):
#     global answer
#     visited[node] = True

#     if dist >= 1 and in_out[node] == "1":
#         answer += 1
#         return

#     for linked_node in adj[node]:
#         if not visited[linked_node]:

#             visited[linked_node] = True
#             dfs(linked_node, dist + 1)
    

# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     in_out = list(sys.stdin.readline().strip("\n"))
#     adj = [[] for _ in range(N)]

#     for _ in range(N - 1):
#         srt, end = map(int, sys.stdin.readline().split())

#         adj[srt - 1].append(end - 1)
#         adj[end - 1].append(srt - 1)

#     for node, info in enumerate(in_out):
#         visited = [False] * (N)

#         if info == "1":
#             dfs(node, 0)

#     print(answer)


import sys
sys.setrecursionlimit(10 ** 7)

answer = 0

def dfs(node):
    global cnt
    visited[node] = True

    for linked_node in adj[node]:
        if not visited[linked_node]:
            if in_out[linked_node] == "1":
                cnt += 1
                continue
            
            visited[linked_node] = True
            dfs(linked_node)
    

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    in_out = list(sys.stdin.readline().strip("\n"))
    adj = [[] for _ in range(N)]
    visited = [False] * (N)
    cnt = 0

    for _ in range(N - 1):
        srt, end = map(int, sys.stdin.readline().split())
        srt -= 1
        end -= 1

        adj[srt].append(end)
        adj[end].append(srt)

        if in_out[srt] == in_out[end] == "1":
            answer += 2

    for node, info in enumerate(in_out):
        if info == "0" and not visited[node]:
            cnt = 0
            dfs(node)
            
            answer += cnt * (cnt -1)

    print(answer)