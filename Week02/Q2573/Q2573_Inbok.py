# import sys
# from collections import deque

# def bfs():
#     queue = deque()
#     melt_list = []
#     visited = [[False for _ in range(M)] for _ in range(N)]

#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] or board[i][j] != 0:
#                 continue
             
#             queue.append((i, j))
#             visited[i][j] = True

#             while queue:
#                 curX, curY = queue.popleft()
                
#                 for idx in range(4):
#                     nextX = curX + move[idx][0]
#                     nextY = curY + move[idx][1]

#                     if is_valid(nextX, nextY) and not visited[nextX][nextY]:
#                         if board[nextX][nextY] != 0:
#                             melt_list.append((nextX, nextY))
#                             continue

#                         visited[nextX][nextY] = True
#                         queue.append((nextX, nextY))

#     melt(melt_list)
#     return count_area()

# def count_area():
#     queue = deque()
#     area = 0
#     visited = [[False for _ in range(M)] for _ in range(N)]

#     for i in range(N):
#         for j in range(M):
#             if area >= 2:
#                 return True

#             if visited[i][j] or board[i][j] == 0:
#                 continue

#             queue.append((i, j))
#             visited[i][j] = True

#             while queue:
#                 curX, curY = queue.popleft()

#                 for idx in range(4):
#                     nextX = curX + move[idx][0]
#                     nextY = curY + move[idx][1]

#                     if is_valid(nextX, nextY) and not visited[nextX][nextY]:
#                         if board[nextX][nextY] == 0:
#                             continue

#                         visited[nextX][nextY] = True
#                         queue.append((nextX, nextY))    
                
#             area += 1

#     return False

# def melt(melt_list):
#     for x, y in melt_list:
#         if board[x][y] == 0:
#             continue
#         board[x][y] -= 1

# def is_valid(x, y):
#     return 0 <= x < N and 0 <= y < M

# if __name__ == "__main__":
#     N, M = map(int, sys.stdin.readline().split())
#     move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     board = []
    
#     for _ in range(N):
#         board.append(list(map(int, sys.stdin.readline().split())))

#     year = 0

#     while True:
#         year += 1

#         if bfs():
#             print(year)
#             break

# 녹을 빙산 좌표
# 구역 확인 함수
# 시간 1년씩 추가
# 최초 2덩어리 이상 되는 시간 서칭
# 다 녹을때까지 2 덩어리 안나오면 0 출력

import sys
from collections import deque

def bfs():
    queue = deque()
    area = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if area >= 2:
                return True

            if visited[i][j] or board[i][j] == 0:
                continue

            queue.append((i, j))
            visited[i][j] = True

            while queue:
                curX, curY = queue.popleft()

                for idx in range(4):
                    nextX = curX + move[idx][0]
                    nextY = curY + move[idx][1]

                    if is_valid(nextX, nextY) and not visited[nextX][nextY]:
                        if board[nextX][nextY] == 0:
                            continue

                        visited[nextX][nextY] = True
                        queue.append((nextX, nextY))    
                
            area += 1

    if area == 0:
        print(0)
        sys.exit()

    return False

def melt():
    del_list = set()

    for key in ice_list:
        x, y = key

        for idx in range(4):
            nextX = x + move[idx][0]
            nextY = y + move[idx][1]

            if is_valid(nextX, nextY):
                if board[nextX][nextY] == 0:
                    if ice_list[key] == 0:
                        del_list.add(key)
                        continue
                    ice_list[key] -= 1

    for key in ice_list:
        x, y = key
        board[x][y] = ice_list[key]

    for x, y in del_list:
        del ice_list[(x, y)]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    board = []
    ice_list = {}
    year = 0

    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))

        for j in range(M):
            if board[i][j] != 0:
                ice_list[(i, j)] = board[i][j]

    while not bfs():
        year += 1
        melt()

    print(year)