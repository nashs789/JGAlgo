import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

# 포인터 2개를 사용해서 이분탐색하는것
# (그 전 점보다)음수면 끝점이동, 양수면 왼쪽점 이동, 
# 스택을 이용해서 가자 작았던 수를 기록해둔다

def sol(start,end):
    temp =[arr[start]+arr[end],arr[start],arr[end]]
    while start < end and start >= 0:
        if abs(arr[start]+arr[end])==0:
            temp = [arr[start]+arr[end],arr[start],arr[end]]
            return temp[1],temp[2]
        elif abs(arr[start]+arr[end]) <= abs(temp[0]):
            temp = [arr[start]+arr[end],arr[start],arr[end]]
        if arr[start] + arr[end] < 0:
            start += 1
        else:
            end -= 1
    return temp[1],temp[2]
print(" ".join(map(str,sol(0,N-1))))