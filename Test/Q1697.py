import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    queue = deque([(N, 0)])
    visited = [False] * 1000001

    while queue:
        cur_node, cur_sec = queue.popleft()

        for next_node in [cur_node + 1, cur_node - 1, cur_node * 2]:
            if cur_node == K:
                print(cur_sec)
                sys.exit()

            if 0 <= next_node <= 100000 and not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, cur_sec + 1))