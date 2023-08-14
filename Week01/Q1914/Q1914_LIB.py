import sys

N = int(sys.stdin.readline())


def hanoi(n, srt, mid, end):
    if n == 0:
        return

    hanoi(n - 1, srt, end, mid)
    print(srt, end)
    hanoi(n - 1, mid, srt, end)


print(pow(2, N) - 1)

if N <= 20:
    hanoi(N, 1, 2, 3)
