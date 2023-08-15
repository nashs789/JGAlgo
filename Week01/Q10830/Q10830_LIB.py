import sys
sys.setrecursionlimit(10**9)


def mul(a, b): # 행렬1, 행렬2
    res = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            for z in range(N):
                res[x][y] += a[x][z] * b[z][y] % 1000

    return res


def calc(a, b): # 행렬, 제곱
    if b == 1:
        return a
    else:
        temp = calc(a, b // 2)
        if b % 2 == 0:
            return mul(temp, temp)
        else:
            return mul(mul(temp, temp), a)


if __name__ == "__main__":
    N, B = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = calc(A, B)

    for row in result:
        for val in row:
            print(val % 1000, end=" ")
        print()
