import sys
from collections import deque

N, K = map(int, input().split())
num = str(input())
count = K
result = []

for i in range(N):
    while count and result:
        if result[-1] < num[i]:
            result.pop()
            count-=1
        else:
            break
    result.append(num[i])

print(''.join(result[:N-K]))