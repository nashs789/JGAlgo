import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())

q = deque([ x for x in range(1,N+1)])

result = []
for _ in range(N):
	for _ in range(K-1):
		q.append(q.popleft())
		print(q)
	result.append(str(q.popleft()))

print('<'+', '.join(result),''+'>')