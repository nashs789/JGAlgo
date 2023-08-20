import sys

def get_idx(num):
    left, right = 0, len(point_list) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if point_list[mid] <= num:
            left = mid + 1
        else: 
            right = mid - 1

    return left - 1

N, M = map(int, sys.stdin.readline().split())
point_list = list(map(int, sys.stdin.readline().split()))

point_list.sort()

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    srt, end = get_idx(x), get_idx(y)
    cnt = end - srt + 1

    if srt == end:
        print(0)
        continue

    if srt < 0 and x > point_list[srt] and point_list[end] > y:
        cnt -= 1

    print(cnt)