# import sys

# input=sys.stdin.readline
# n,k=map(int,input().split())
# x = [(0,0)]
# d = [[0]*(k+1) for _ in range(n+1)]

# for knap_weight in range(n):
#     item_weight,item_value =list(map(int,input().split()))
#     x.append((item_weight,item_value))

# for knap_weight in range(1,n+1):
#     for j in range(1,k+1):
#         item_weight = x[knap_weight][0]
#         item_value = x[knap_weight][1]

#         if j<item_weight:
#             d[knap_weight][j]=d[knap_weight-1][j]
#         else:
#             d[knap_weight][j]=max(d[knap_weight-1][j],d[knap_weight-1][j-item_weight]+item_value)

# print(d[n][k])

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
for knap_weight in range(n):
    item_weight, item_value = map(int, input().split())
    bag.append((item_weight, item_value))

dp = [0] * (k + 1)
#print(dp)
for item in bag:
    item_weight, item_value = item
    #print("wei = ", item_weight, "    val = ", item_value)
    for knap_weight in range(k, item_weight - 1, -1):  # w까지 보고 싶기 때문에 -1 해줍니다.
        dp[knap_weight] = max(dp[knap_weight], dp[knap_weight - item_weight] + item_value)
    #print(dp)
print(dp[-1])

print(dp)   