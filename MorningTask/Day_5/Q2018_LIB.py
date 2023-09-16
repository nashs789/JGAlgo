# ==================== 시간 초과[ 구간 합 + 투 포인터 ] ==================== 
# import sys

# N = int(input())

# num_list = [num for num in range(1, N + 1)]
# prefix_sum = [0 for _ in range(N)]
# prefix_sum[0] = num_list[0]
# ans, left, right = 0, 0, 1

# for idx in range(1, N):
#     prefix_sum[idx] = prefix_sum[idx - 1] + num_list[idx]

#     if prefix_sum[idx] == N:
#         ans += 1

# while left < right:
#     gap = prefix_sum[right] - prefix_sum[left]

#     if gap == N:
#         ans += 1

#     if gap < N:
#         right += 1
#     else:
#         left += 1

# print(ans)

# ==================== 문제 해결[ 투 포인터 개념? ] ==================== 
import sys
from heapq import heappop, heappush

N = int(input())
cur_sum = 0
ans = 0
queue = []

for num in range(1, N + 1):
    heappush(queue, num)
    cur_sum += num

    while cur_sum >= N:
        if cur_sum == N:
            ans += 1 

        cur_sum -= heappop(queue)

print(ans)

# ==================== 문제 해결[ 책 ] ====================
# import sys

# N = int(input())
# cnt, srt, end, sum = 1, 1, 1, 1

# while end != N:
#     if sum == N:
#         cnt += 1
#         end += 1
#         sum += end
#     elif sum > N:
#         sum -= srt
#         srt += 1
#     else:
#         end += 1
#         sum += end

# print(cnt)