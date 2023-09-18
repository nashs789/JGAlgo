import sys
import math

input = sys.stdin.readline
A, B, V = map(int, input().split())

daily_distance = A - B
days = math.ceil((V - A) / daily_distance) + 1
print(days)

# 시간초과;
# cnt = 0
# height = 0

# while True:
#     cnt += 1
#     height += A
#     if height >= V:
#         break
#     height -= B

# print(cnt)
