import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for x in range(N)]


# 시작점 + 끝점 값을 저장
# 재귀함수를 이용해서 왼쪽서치, 오른쪽 서치
# 이후 값이 작지 않다면 서치종료후 들어가기 전 값들 프린트
# 만약 작다면 서치하러 파고파고 들어가기
left = arr[0]
right = arr[-1]
target = arr[0] + arr[-1]
def binary(s,e):
    global left,right,target
    mid = (s+e)//2
    if abs(arr[s]+arr[e]) < target:
        left = arr[s]
        right = arr[e]
    binary(s,mid)
    binary(mid,e)