import sys
from collections import deque

def dfs(arr, node):
    global cnt

    for linked_node in arr[node]:
        if not visited[linked_node]:
            visited[linked_node] = True
            cnt += 1
            dfs(arr, linked_node)

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    mid = (N + 1) // 2
    answer = 0
    bigger_list = [[] for _ in range(N + 1)]
    smaller_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        big, small = map(int, input().split())
        bigger_list[small].append(big)
        smaller_list[big].append(small)

    for node in range(N + 1):
        visited = [False] * (N + 1)
        cnt = 0
        dfs(bigger_list, node)

        if cnt >= mid:
            answer += 1

        cnt = 0
        dfs(smaller_list, node)

        if cnt >= mid:
            answer += 1
    
    print(answer)