import sys 
input = sys.stdin.readline

N = int(input())
stacks = []
for i in range(N):
	order = list(map(str,input().split()))
	if order[0]=="push":
		stacks.append(int(order[1]))
	elif order[0]=="pop":
		if len(stacks)==0:
			print(-1)
		else:
			print(stacks.pop())
			
	elif order[0]=="size":
		print(len(stacks))
	elif order[0]=="empty": 
		if len(stacks)==0:
			print(1)
		else:
			print(0)
	else: 
		if len(stacks)==0:
			print(-1)
		else:
			print(stacks[-1])
	order = []