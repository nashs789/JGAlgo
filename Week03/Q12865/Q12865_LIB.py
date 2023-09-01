# import sys
# input = sys.stdin.readline

# if __name__ == "__main__":
#     N, K = map(int, input().strip().split())
#     dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
#     items = [(0, 0)]

#     for _ in range(N):
#         weight, value = map(int, input().strip().split())
#         items.append((weight, value))

#     for item_no, item in enumerate(items):
#         weight, value = item[0], item[1]

#         for target_weight in range(1, K + 1):
#             prev_item = dp[item_no - 1]    # 이전 물건

#             if target_weight < weight:
#                 dp[item_no][target_weight] = prev_item[target_weight]
#             else:
#                 dp[item_no][target_weight] = max(prev_item[target_weight], value + prev_item[target_weight - weight])
        
#     print(dp[N][K])

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    knapsack = [0 for _ in range(K + 1)]
    items = [(0, 0)]

    for _ in range(N):
        weight, value = map(int, input().strip().split())
        items.append((weight, value))

    for item_weight, item_value in items:
        for weight in range(K, -1, -1):
            if item_weight > weight:
                break
            
            knapsack[weight] = max(knapsack[weight], knapsack[weight - item_weight] + item_value)
    
    print(knapsack[-1])