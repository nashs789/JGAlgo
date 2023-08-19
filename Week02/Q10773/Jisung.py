import sys 
input = sys.stdin.readline

N = int(input())
stacks = []
for i in range(N):
	num = int(input())
	if num==0:
		stacks.pop()
	else:
		stacks.append(num)
print(sum(stacks))