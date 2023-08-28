import sys
input = sys.stdin.readline

if __name__ == "__main__":
    S = input().strip()
    s_len = len(S)
    N = int(input())
    A = [input().strip() for _ in range(N)]
    dp = [False for _ in range(s_len + 1)]
    dp[0] = True

    for i in range(s_len):
        if dp[i]:
            for word in A:
                if S[i: i + len(word)] == word:
                    dp[i + len(word)] = True

    result = dp[s_len]
    print(int(result))