import sys
from collections import deque

def game_start():
    direction = 0    # 우, 하, 좌, 상
    sec = 1
    head = (0, 0)
    snake = deque([(0, 0)])

    while True:
        cur_loc = head
        curX = cur_loc[0]
        curY = cur_loc[1]
        nextX = curX + move[direction][0]
        nextY = curY + move[direction][1]

        if N <= nextX or nextX < 0 or N <= nextY or nextY < 0:
            print(sec)
            break

        head = (nextX, nextY)
        
        if head in snake:
            print(sec)
            break
            
        snake.append(head)
        
        if not board[nextX][nextY]:
            snake.popleft()
        else:
            board[nextX][nextY] = False

        if str(sec) in reg:
            next_direction = reg[str(sec)]

            if next_direction == "D":
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
            else:
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1

        sec += 1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    board = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[x - 1][y - 1] = True

    L = int(sys.stdin.readline())
    reg = dict()

    for _ in range(L):
        sec, direction = sys.stdin.readline().split()
        reg[sec] = direction

    game_start()