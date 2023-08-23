import sys
from collections import deque

def bfs():
    queue = deque(tomatoes)

    while queue:
        cur_h, cur_n, cur_m = queue.popleft()
        last_day = box[cur_h][cur_n][cur_m]

        for h, n, m in move:
             next_h, next_n, next_m = cur_h + h, cur_n + n, cur_m + m

             if is_valid(next_h, next_n, next_m) and box[next_h][next_n][next_m] == 0:
                box[next_h][next_n][next_m] = box[cur_h][cur_n][cur_m] + 1
                queue.append((next_h, next_n, next_m))

    for h in box:
        for n in h:
            for m in n:
                if m == 0:
                    print(-1)
                    sys.exit()

    print(last_day - 1)

def is_valid(h, n, m):
    return 0 <= h < H and 0 <= n < N and 0 <= m < M    

if __name__ == "__main__":
    input = sys.stdin.readline
    M, N, H = map(int, input().split())
    move = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    tomatoes = []
    box = []

    for h in range(H):
        row = []
        for n in range(N):
            row.append(list(map(int, input().split())))

            for m in range(M):
                if row[n][m] == 1:
                    tomatoes.append((h, n, m))
        box.append(row)
    bfs()