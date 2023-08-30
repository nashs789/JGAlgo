import sys
input = sys.stdin.readline

N = int(input())
matrix = []
dp = [[0] * (N) for _ in range(N)]

for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(1, N): # 몇 번째 대각선?
    for j in range(0, N-i): # 대각선에서 몇 번째 열?
        if i == 1:
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue
        
        dp[j][j+i] = sys.maxsize #(최댓값으로 배치)
        for k in range(j, j+i):
            print(j, j+i)
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

print(dp[0][N-1])