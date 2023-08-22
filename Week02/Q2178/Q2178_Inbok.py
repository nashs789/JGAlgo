import sys
from collections import deque

def bfs():
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    visited[0][0] = True
    queue.append(((0, 0), 1))    # ((x, y), dist)

    while queue:
        cur_node = queue.popleft()
        curX, curY = cur_node[0]
        cur_dist = cur_node[1]

        if curX == N - 1 and curY == M - 1:
            print(cur_dist)
            return

        for idx in range(4):
            nextX = curX + move[idx][0]
            nextY = curY + move[idx][1]

            if is_valid(nextX, nextY) and not visited[nextX][nextY] and maze[nextX][nextY] == 1:
                visited[nextX][nextY] = True
                queue.append(((nextX, nextY), cur_dist + 1))

        
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().strip("\n"))))

    bfs()