import sys

givenNum = int(sys.stdin.readline())

givenList = list(map(int,sys.stdin.readline().split())) # 6 9 5 7 4

stack = []
result = [0] * givenNum

for i in range(givenNum) :
    tower = givenList[i]
    while stack and givenList[stack[-1]] < tower :
        stack.pop()
    if stack:
        result[i] = stack[-1] +1
    stack.append(i)
        
print(' '.join(list(map(str, result))))


# n = int(sys.stdin.readline())
# tower = list(map(int, sys.stdin.readline().split()))
# stack = []
# goto = [0] * n

# for i in range(n):
#     t = tower[i]
#     while stack and tower[stack[-1]] < t:
#         stack.pop()
#     if stack:
#         goto[i] = stack[-1] + 1
#     stack.append(i)

# print(' '.join(list(map(str, goto))))