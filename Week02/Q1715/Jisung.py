import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
temp = []
result = 0

for i in range(N):
    nums = int(input())
    hq.heappush(temp,nums)

for j in range(N):
	if j%2==0:
		result += result + (hq.heappop(temp))
	else:
		result += (hq.heappop(temp))
print(result)