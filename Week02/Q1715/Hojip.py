import sys
import heapq
givenNum = int(sys.stdin.readline())

givenList = list()
for i in range(givenNum) :
    heapq.heappush(givenList, int(sys.stdin.readline()))

result = int()
while True :
    if len(givenList) == 1:
        print(result)
        break
    first = heapq.heappop(givenList)
    sec = heapq.heappop(givenList)
    total = first+sec
    result += total
    heapq.heappush(givenList, total)

# if len(givenList) == 1:
#     print(givenList[0])
# else:
#     result = int()
#     for i in range(givenNum-1) : # 20 20
#         if len(givenList) == 1 :
#             print(result)
#             break
#         tmpList = []
#         while True :
#             if len(givenList) == 0 :
#                 break
#             tmpResult = int()
#             if len(givenList) == 1 :
#                 tmpResult =  heapq.heappop(givenList)
#             else :
#                 tmpResult = heapq.heappop(givenList)
#                 tmpResult += heapq.heappop(givenList)
#                 result += tmpResult
#             heapq.heappush(tmpList, tmpResult)
#         givenList = tmpList


