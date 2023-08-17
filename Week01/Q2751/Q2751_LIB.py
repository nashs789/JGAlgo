import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    pos_arr = [False] * 1000001
    neg_arr = [False] * 1000001

    for _ in range(N):
        num = int(sys.stdin.readline())

        if num >= 0:
            pos_arr[num] = True
        else:
            neg_arr[abs(num)] = True

    for idx, val in reversed(list(enumerate(neg_arr))):
        if val:
            print(-1 * idx)

    for idx, val in enumerate(pos_arr):
        if val:
            print(idx)
