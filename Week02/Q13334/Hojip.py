import sys
import heapq

givenNum = int(sys.stdin.readline())

givenList = list() #

for i in range(givenNum) :
    A, B = map(int,sys.stdin.readline().split())
    start, end = min(A,B), max(A,B)
    givenList.append((start, end))

Distance = int(sys.stdin.readline())

heap = []

givenList.sort(key=lambda x: x[1]) # 끝나는 지점 기준 오름차순 정렬

result = 0

for i in givenList :
    start, end = i
    heapq.heappush(heap, start)
    while True :
        if len(heap) != 0 and heap[0] < end - Distance :
            heapq.heappop(heap)
        else :
            break
    result = max(result, len(heap))

print(result)

#-----------------------------------------------------
#GPT

# import sys
# import heapq

# givenNum = int(sys.stdin.readline())

# givenList = []

# for _ in range(givenNum):
#     A, B = map(int, sys.stdin.readline().split())
#     start, end = min(A, B), max(A, B)
#     givenList.append((start, end))

# # 철로의 길이
# Distance = int(sys.stdin.readline())

# # 끝나는 지점을 기준으로 정렬
# givenList.sort(key=lambda x: x[1])

# result = 0
# # 시작 지점을 저장할 최소 힙
# start_points = []

# for house in givenList:
#     start, end = house
#     # 철로 길이 내에 있는 집의 시작 지점을 힙에 추가
#     heapq.heappush(start_points, start)
#     # 철로 길이를 벗어나는 집의 시작 지점을 힙에서 제거
#     while start_points and start_points[0] < end - Distance:
#         heapq.heappop(start_points)
#     # 현재 철로 길이 내에 있는 집의 수를 결과와 비교
#     result = max(result, len(start_points))

# print(result)


#--------------------------------------------------------------
# import sys
# import heapq
# givenNum = int(sys.stdin.readline())

# givenList = list() #

# for i in range(givenNum) :
#     A, B = map(int,sys.stdin.readline().split())
#     if A < B :
#         heapq.heappush(givenList, (A, B))
#     else :
#         heapq.heappush(givenList, (B, A))

# Distance = int(sys.stdin.readline())

# givenResultList = [] #

# for i in givenList :
#     tmpDistance = i[1]-i[0]
#     if tmpDistance > Distance :
#         continue
#     else :
#         heapq.heappush(givenResultList, i)
        

# resultList = [] # 
# for i in range(len(givenResultList)) :
#     tmpLength = []
#     firstMin = givenResultList[0] # 30 50
#     Distance = firstMin[0]+Distance # 70
#     result = int()
#     while True :
#         if len(givenResultList) == 0:
#             break
#         tmpTuple = givenResultList[0] #50 60
#         first = tmpTuple[0] # 50
#         last = tmpTuple[1] # 60
#         if firstMin[0] <= first and last <= Distance :
#             result += 1
#             heapq.heappop(givenResultList)
#         else :
#             tmpLength.append(heapq.heappop(givenResultList))
#             continue
#     resultList.append(result)
#     givenResultList += tmpLength
#     heapq.heapify(givenResultList)
#     if len(givenResultList) == 0:
#         break
# if len(resultList) == 0 :
#     print(0)
# else :
#     print(max(resultList))