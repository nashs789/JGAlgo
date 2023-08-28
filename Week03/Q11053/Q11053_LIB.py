import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num_list = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(0, i):
            if num_list[i] > num_list[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
        
    print(max(dp))