# import sys
# import math

# def is_prime(n):
#     if n == 1:
#         return False

#     sqrt = int(math.sqrt(n)) + 1
#     for idx in range(2, sqrt):
#         if n % idx == 0:
#             return False

#     return True

# T = int(sys.stdin.readline())

# for _ in range(T):
#     num = int(sys.stdin.readline())
#     minV = sys.maxsize
#     minAns = 0 
#     maxAns = 0 

#     List = list(range(2, num + 1))
#     List = list(filter(is_prime, List));

#     for item in List:
#         num2 = num - item
#         gap = abs(item - num2)

#         if is_prime(num2) and minV > gap:
#             minV = gap
#             minAns = min(num2, item)
#             maxAns = max(num2, item)

#     print(minAns, " ", maxAns)

################################ 에라토네스의 채 사용 해야할듯 ################################

# import sys
# import math

# def is_prime(n):
#     if n == 1:
#         return False

#     sqrt = int(math.sqrt(n)) + 1
#     for idx in range(2, sqrt):
#         if n % idx == 0:
#             return False

#     return True

# T = int(sys.stdin.readline())
# prime_list = [False for _ in range(10001)]

# for idx in range(2, len(prime_list)):
#     if prime_list[idx]:
#         continue

#     if is_prime(idx):
#         prime_list[idx] = False
#         next_prime = idx;

#         while next_prime < 10001:
#             prime_list[idx] = True
#             next_prime += idx

# for _ in range(T):
#     num = int(sys.stdin.readline())
#     minV = sys.maxsize
#     minAns = 0 
#     maxAns = 0 

#     List = list(range(2, num + 1))

#     for item in range(1, num + 1):
#         if not prime_list[item]:
#             continue

#         num2 = num - item
#         gap = abs(item - num2)

#         if is_prime(num2) and minV > gap:
#             minV = gap
#             minAns = min(num2, item)
#             maxAns = max(num2, item)

#     print(minAns,maxAns)

import sys
import math

T = int(sys.stdin.readline())
prime_list = [False for _ in range(10001)]

for idx in range(2, len(prime_list)):
    if prime_list[idx]:
        continue

    next_prime = idx + idx
    if idx > 1000:
        break

    while next_prime < 10001:
        prime_list[next_prime] = True
        next_prime += idx

for _ in range(T):
    num = int(sys.stdin.readline())

    List = list(range(2, num + 1))
    bound = int(num / 2)

    for item in range(bound, 0, -1):
        if prime_list[item]:
            continue

        gap = num - item

        if not prime_list[gap]:
            print(min(gap, item), max(gap, item))
            break