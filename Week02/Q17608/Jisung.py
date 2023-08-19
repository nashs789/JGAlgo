import sys 
input = sys.stdin.readline

N = int(input())
stacks = []
for _ in range(N):
	stacks.append(int(input()))
high = 0
count = 0
for _ in range(N):
	newbar = stacks.pop()
	if newbar > high:
		count += 1
		high = newbar
		
print(count)
	