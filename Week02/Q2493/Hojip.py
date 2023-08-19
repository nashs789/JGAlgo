import sys

givenNum = int(sys.stdin.readline())

givenList = list(map(int,sys.stdin.readline().split())) # 6 9 5 7 4

stack = []

resultList = [0] * givenNum

for i in range(givenNum) :
    tower = givenList[i]
    while True :
        if stack != 0 and givenList[stack[-1]] < tower :
            stack.pop()
        if stack != 0 :
            resultList[i] = stack[-1] + 1
        
print(resultList)

for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        stack.pop()
    if stack:
        goto[i] = stack[-1] + 1
    stack.append(i)