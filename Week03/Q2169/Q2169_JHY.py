import sys

# 행렬 크기 입력
n, m = map(int, sys.stdin.readline().split())

# DP 테이블
dp = []

# DP 테이블에 각 행 추가
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

# DP 테이블의 첫 번째 행 업데이트
for j in range(1, m):
    dp[0][j] += dp[0][j-1]

# DP 테이블의 나머지 행 업데이트
for i in range(1, n):
    # 두가지 임시 배열 생성
    left_to_right = dp[i][:] # 왼쪽에서 오른쪽으로 가는 경우
    right_to_left = dp[i][:] # 오른쪽에서 왼쪽으로 가는 경우

    # 왼쪽에서 오른쪽으로 가는 경우 업데이트
    for j in range(m):
        # 첫번째 열일 경우, 위에서 오는 경우 밖에 없으므로
        if (j == 0):
            left_to_right[j] += dp[i-1][j]
        # 나머지 열에 대해, 위에서 내려오는 경우와 왼쪽에서 오는 경우를 비교
        else:
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])

    # 오른쪽에서 왼쪽으로 가는 경우 업데이트
    for j in range(m-1, -1, -1):
        # 마지막 열일 경우, 위에서 오는 경우 밖에 없으므로
        if (j == m-1):
            right_to_left[j] += dp[i-1][j]
        # 나머지 열에 대해, 위에서 내려오는 경우와 오른쪽에서 오는 경우를 비교
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

    # 두 가지 임시 배열을 비교해, 각 좌표값들을 최대값으로 업데이트
    for j in range(m):
        dp[i][j] = max(left_to_right[j], right_to_left[j])


for row in dp:
    formatted_row = " ".join("{:>4}".format(value) for value in row)
    print(formatted_row)

print(dp[n-1][m-1])