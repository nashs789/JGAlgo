import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().strip().split())) for _ in range(N)]

    for col in range(1, M):
        board[0][col] += board[0][col - 1]

    for row in range(1, N):
        left_temp = [board[row][col] + board[row - 1][col] for col in range(M)]
        right_temp = [board[row][col] + board[row - 1][col] for col in range(M)]

        for col in range(1, M):
            left_temp[col] = max(left_temp[col], left_temp[col - 1] + board[row][col])

        for col in range(M - 2, -1, -1):
            right_temp[col] = max(right_temp[col], right_temp[col + 1] + board[row][col])

        for col in range(M) : 
            board[row][col] = max(left_temp[col], right_temp[col])

print(board[-1][-1])