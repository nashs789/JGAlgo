import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline()) 
    dp = [0 for _ in range(num + 1)]
    dp[0] = 1
    dp[1] = 1

    for idx in range(2, num + 1):
        dp[idx] = (dp[idx - 2] + dp[idx - 1]) % 15746

    print(dp[num])