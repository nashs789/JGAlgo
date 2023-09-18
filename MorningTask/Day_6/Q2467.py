import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

# 포인터 2개를 사용해서 이분탐색하는것
# (그 전 점보다)음수면 끝점이동, 양수면 왼쪽점 이동, 

def sol(start,end):
    temp = 0
    while start < end and start >= 0 and end<=len(arr)-1:
        if arr[start] + arr[end] > temp:
            start += 1
        else:
            end += 1
        temp = arr[start]+arr[end]
        if temp == 0:
            return arr[start], arr[end]
    return arr[start],arr[end]
sol(0,1)
        