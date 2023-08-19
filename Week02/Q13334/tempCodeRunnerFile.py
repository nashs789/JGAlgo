import sys
import heapq
givenNum = int(sys.stdin.readline())

givenList = list() #

for i in range(givenNum) :
    A, B = map(int,sys.stdin.readline().split())
    if A < B :
        heapq.heappush(givenList, (A, B))
    else :
        heapq.heappush(givenList, (B, A))

Distance = int(sys.stdin.readline())

givenResultList = [] #

for i in givenList :
    tmpDistance = i[1]-i[0]
    if tmpDistance > Distance :
        continue
    else :
        heapq.heappush(givenResultList, i)
        
print(givenResultList) # [(10, 20), (10, 25), (25, 30), (30, 50), (50, 60), (25, 35), (80, 100)]

resultList = [] # 
for i in range(len(givenResultList)) :
    firstMin = givenResultList[0] # 30 50
    Distance = firstMin[0]+Distance # 70
    result = int()
    while True :
        if len(givenResultList) == 0:
            break
        tmpTuple = givenResultList[0] #50 60
        first = tmpTuple[0] # 50
        last = tmpTuple[1] # 60
        if firstMin[0] <= first and last <= Distance :
            result += 1
            heapq.heappop(givenResultList)
        else :
            break
    resultList.append(result)
    if len(givenResultList) == 0:
        break

print(max(resultList))