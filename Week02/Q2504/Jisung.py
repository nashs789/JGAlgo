import sys 
input = sys.stdin.readline

console = 1
stacks = []
contemp = 0
result = 0
temp = str(input().rstrip())

def sol(console,stacks,contemp,result):
	for i in range(len(temp)):
		if temp[i] =="(":
			console *= 2
			stacks.append(temp[i])
			contemp = True
		elif temp[i] =="[":
			console *= 3
			stacks.append(temp[i])
			contemp = True
		elif temp[i] ==")":
			if len(stacks)==0 or stacks[-1] !="(":
				return 0
			else:
				stacks.pop()
				if contemp:
					result += console
					contemp = False
				console = console//2
		elif temp[i]=="]":
			if len(stacks)==0 or stacks[-1] !="[":
				return 0
			else:
				stacks.pop()
				if contemp:
					result += console
					contemp = False
				console = console//3
	if len(stacks)==0:
		return result
	else:
		return 0

print(sol(console,stacks,contemp,result))