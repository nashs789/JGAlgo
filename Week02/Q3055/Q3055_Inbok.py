import sys
from collections import deque

def bfs(srt):
    queue = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    srtX, srtY, sec = srt
    queue.append(srt)
    visited[srtX][srtY] = True

    while queue:
        curX, curY, cur_sec = queue.popleft()

        if cur_sec == sec + 1:
            flood()
            sec += 1

        # 이동 했었는데 물이 차는 경우 (물이 찰 예정인 칸)
        if board[curX][curY] == "*":
            continue

        if board[curX][curY] == "D":
            print(cur_sec)
            sys.exit()

        for x, y in move:
            nextX = curX + x
            nextY = curY + y        

            if is_valid(nextX, nextY) and not visited[nextX][nextY] and (board[nextX][nextY] == "." or board[nextX][nextY] == "D"):
                queue.append((nextX, nextY, cur_sec + 1))
                visited[nextX][nextY] = True

    print("KAKTUS")

def flood():
    cur_len = len(water_list)

    for _ in range(cur_len):
        curX, curY = water_list.popleft()
        
        for x, y in move:
            nextX = curX + x
            nextY = curY + y
            
            if is_valid(nextX, nextY) and board[nextX][nextY] == ".":
                board[nextX][nextY] = "*"
                water_list.append((nextX, nextY))        
 
def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C

if __name__ == "__main__":
    input = sys.stdin.readline
    R, C = map(int, input().split())
    water_list = deque()
    board = []
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cur_point = None

    for i in range(R):
        row = list(input().strip("\n"))
        board.append(row)

        for j in range(C):
            if board[i][j] == "*":
                water_list.append((i, j))
            elif board[i][j] == "S":
                cur_point = (i, j, 0)

    bfs(cur_point)

# . 비어있음
# * 물
# D 비버굴
# S 고슴도치
# X 돌