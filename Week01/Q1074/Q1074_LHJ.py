def Z(N, r, c, visit):
    if N == 0:
        return visit

    mid = 2** (N) //2 # 4
    
    # 1사분면
    if r < mid and c < mid:
        return Z(N-1, r, c, visit)

    # 2 사분면
    elif r < mid and c >= mid:
        return Z(N-1, r, c-mid, visit+mid**2)

    # 3사분면
    elif r >= mid and c < mid:
        return Z(N-1, r-mid, c, visit+(mid**2)*2)

    # 4 사분면
    else:
        return Z(N-1, r-mid, c-mid, visit+(mid**2)*3)

# 분할 할 때마다 r과 c를 1사분면 (0,0) 위치에 배치한다.
# visit : 각 사분면마다 (0,0) 에 위치한 방문 횟수를 더해준다.
import sys
N, r, c = map(int, sys.stdin.readline().split())
print(Z(N, r, c, 0))