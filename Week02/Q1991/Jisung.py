import sys

input = sys.stdin.readline

N = int(input())
binary = {}
for _ in range(N):
	root,left,right = map(str,input().split())
	binary[root] = left,right

def before(root):
	if root=='.':
		return
	else:
		print(root, end="")
		if binary[root]!='.':
			before(binary[root][0])
		if binary[root]!='.':
			before(binary[root][1])

def middle(root):
	if root=='.':
		return
	else:
		if binary[root]!='.':
			middle(binary[root][0])
		print(root, end="")
		if binary[root]!='.':
			middle(binary[root][1])
			
def after(root):
	if root=='.':
		return
	else:
		if binary[root]!='.':
			after(binary[root][0])
		if binary[root]!='.':
			after(binary[root][1])
		print(root, end="")

before('A')
print(end="\n")
middle('A')
print(end="\n")
after('A')