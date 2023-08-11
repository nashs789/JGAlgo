import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
# aD - b(D-1) > V

print(math.ceil((v-b)/(a-b)))



# def plus_meter(meter, count):
#     if(meter >= v):
#         print(count)
#     else:
#         meter += (a-b)
#         count += 1
#         plus_meter(meter, count)
# plus_meter(a, 1)


# count = 1
# meter = a
# for _ in range(1000000000):
#     meter+=(a-b)
#     count+=1
#     if meter >= v:
#         break
# print(count)