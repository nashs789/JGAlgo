import sys
input = sys.stdin.readline

# 0 0 0 0 0
# 0 1 2 3 4
# 0 2 4 6 8
# 0 3 6 9 12
# 0 4 8 12 16
# N*N?을 기준으로 갯수가 생기니까 일단 이거보다는 적다
# 그러고 K가 뭐보다 큰지 확인해야함

N = int(input())
K = int(input())

def binary_search(target, start, end):
    while(start<=end):
        mid = (start+end)//2
        cnt = 0
        for i in range(1,N+1):
            cnt+= min(mid//i,N)
        if cnt >= target:
            end = mid-1
        else:
            start = mid+1
    return start
print(binary_search(K,1,N*N))