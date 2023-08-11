# import sys

# up, down, target = map(int, sys.stdin.readline().split())
# day = 0
# curPos = 0

# while True:
#     day += 1
#     curPos += up

#     if curPos >= target:
#         print(day)
#         break
    
#     curPos -= down

import math
import sys

up, down, target = map(int, sys.stdin.readline().split())
print(math.ceil((target - down) / (up - down)))