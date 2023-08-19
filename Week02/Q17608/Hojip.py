import sys

givenNum = int(sys.stdin.readline())

givenList = list()
for i in range(givenNum) :
    givenList.append(int(sys.stdin.readline()))

maxTmp = 0

cnt = 1
while True :
    if maxTmp < givenList[-1] :
        cnt+= 1
        maxTmp = max(maxTmp, givenList.pop())
    else :
        maxTmp = max(maxTmp, givenList.pop())
    
    if len(givenList) == 0 :
        break
print(cnt)