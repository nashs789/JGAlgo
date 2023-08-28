import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len
        # 시작점과 끝점이 같다면 글자수가 1개이므로 무조건 팰린드롬
        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
        	# 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end: 
                dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])