import sys
input = sys.stdin.readline

str_order = str(input().rstrip())
stack = []
check = True

for i in str_order:
    stack.append(i)
    if len(stack)>=4:
        if stack[-4:] == ["P","P","A","P"]:
            for i in range(3):
                stack.pop()

if len(stack)==0:
    print("PPAP")
else:
    print("NP")
