import sys
from collections import deque

def bfs(day):
    queue = deque(tomatoes)

    while queue:
        cur_h, cur_n, cur_m = queue.popleft()

        for h, n, m in move:
             next_h, next_n, next_m = cur_h + h, cur_n + n, cur_m + m

             if is_valid(next_h, next_n, next_m) and box[next_h][next_n][next_m] == 0:
                box[next_h][next_n][next_m] = day + 1
                queue.append((next_h, next_n, next_m))

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return False
    
    return True

    # 영역이 다 칠해졌는제 확인 len(queue)
    # print(day)

       
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

    day = 1

    while True:
        if bfs(day):
            print(day)
            break

        day += 1