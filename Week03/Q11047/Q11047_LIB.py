import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    coins = []
    cnt = 0

    for _ in range(N):
        coins.append(int(input().strip()))

    for idx in reversed(range(N)):
        cnt += K //coins[idx]
        K %= coins[idx]

    print(cnt)