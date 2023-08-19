import sys 
input = sys.stdin.readline

N = int(input())
for _ in range(N):
	stacks = []
	a = str(input().rstrip())
	for i in a:
		if i=="(":
			stacks.append(i)
		elif i==")":
			try:
				stacks.pop()
			except:
				stacks.append(1)	
				break
	if len(stacks)>0:
		print("NO")
	else:
		print("YES")