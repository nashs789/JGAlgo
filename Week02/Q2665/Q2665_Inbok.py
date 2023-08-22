import sys
import heapq

def dijkstra(srtX, srtY, broke_count):
    pQueue = [(srtX, srtY, broke_count)]
    broke[srtX][srtY] = 0

    # 1은 흰방 0은 검은방
    while pQueue:
        curX, curY, cur_broke = heapq.heappop(pQueue)

        if broke[curX][curY] < cur_broke:
            continue

        for idx in range(4):
            nextX = curX + move[idx][0]
            nextY = curY + move[idx][1]

            if not is_valid(nextX, nextY):
                continue
            
            wall = 0
            if maze[nextX][nextY] == 0:
                wall = 1

            next_broke = cur_broke + wall

            if broke[nextX][nextY] > next_broke:
                broke[nextX][nextY] = next_broke
                heapq.heappush(pQueue, (nextX, nextY, next_broke))

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    maze = []
    broke = [[sys.maxsize for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        maze.append(list(map(int, input().strip("\n"))))

    dijkstra(0, 0, 0)    # x, y ,broke
    print(broke[N - 1][N - 1])