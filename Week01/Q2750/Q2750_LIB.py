# 책에서 가장 먼저 나옴
# 1000 x 1000 사이즈

import sys


def bubble_sort(n):
    for i in range(n - 1):
        sorted_cnt = 0
        for j in range(0, n - 1 - i):
            if num_list[j] > num_list[j + 1]:
                sorted_cnt += 1
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

        if sorted_cnt == 0:
            break


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num_list = list()

    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))

    bubble_sort(N)

    for idx, val in enumerate(num_list):
        print(val)
