# import sys
# from queue import PriorityQueue
# from heapq import heappush, heappop

# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     data, pQueue = [], []

#     for _ in range(N):
#         x, y = map(int, sys.stdin.readline().split())
#         if x > y:
#             x, y = y, x
#         data.append((x, y - x))

#     L = int(sys.stdin.readline())
#     max_cnt = 0

#     for val in data:
#         if val[1] <= L:
#             heappush(pQueue, val)

#     while len(pQueue) != 0:
#         target = heappop(pQueue)
#         temp = []    # priorty queue 에서 뽑은 수중에 다시 넣을 숫자 임시 저장
#         cnt = 1

#         if target[1] > L:
#             continue

#         # queue가 비어있지 않음 
#         while len(pQueue) != 0:
#             next = heappop(pQueue)

#             if target[0] <= next[0] <= target[0] + L and next[0] + next[1] <= target[0] + L:
#                 cnt += 1

#             # 시작점이 같은 좌표가 아닐때만 queue에 다시 넣기 위한 준비
#             if next[0] != target[0]:
#                 temp.append(next)

#         max_cnt = max(max_cnt, cnt)

#         for val in temp:
#             heappush(pQueue, val)

#     print(max_cnt)

import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    info_list = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        if x > y:
            x, y = y, x
        info_list.append((x, y))

    L = int(sys.stdin.readline())
    info_list.sort(key = lambda y : (y[1], y[0]))
    max_val = 0
    roads = []

    for val in info_list:
        srt, end = val
        heappush(roads, srt)

        while roads and roads[0] < end - L:
            heappop(roads)

        max_val = max(max_val, len(roads))
    
    print(max_val)