import sys

if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    len_s = len(string)
    dp = [[False for _ in range(len_s)] for _ in range(len_s)]

    for idx in range(len_s):
        dp[idx][idx] = True

    for idx in range(len_s - 1):
        if string[idx] == string[idx + 1]:
            dp[idx][idx + 1] = True

    for i in range(len_s - 2):
        for srt in range(len_s - 2 - i):
            end = srt + i + 2

            if string[srt] == string[end] and dp[srt + 1][end - 1]:
                dp[srt][end] = True

    result = [0 for _ in range(len_s)]
    result[0] = 1

    for i in range(1, len_s):
        min_val = result[i - 1] + 1

        for j in range(i):
            if dp[j][i]:
                min_val = min(min_val, result[j - 1] + 1)
            result[i] = min_val

    print(result[-1])