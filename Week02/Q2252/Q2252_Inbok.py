import sys
sys.setrecursionlimit(10 ** 5)

def dfs(node):    
    visited[node] = True

    for linked_node in adj[node]:
        if not visited[linked_node]:
            dfs(linked_node)
    
    print(node, end=" ")

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        adj[B].append(A)

    for node in range(1, N + 1):
        if not visited[node]:
            dfs(node)