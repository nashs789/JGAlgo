# 이분탐색 left right 
# 일단 처음과 마지막에는 설치
# 공유기의 거리 계산 = 1 ,4, 9 = 거리는 3 
# 공유기를 설치할 거리를 이분탐색으로 결정하기
import sys
input = sys.stdin.readline
N, C =  map(int,input().split()) # 5 3
house = list(int(input().rstrip()) for _ in range(N));
# 집들의 거리는 일직선에 위치함.
print(house)
house.sort(); #[1,2,4,8,9]

start, end = 1, house[N-1] - house[0]; # 1, 8
# 집사이의 최소거리, 최대거리
# 이떄 최대거리의 계산은 가장 큰값이 아니라 '집 간의 가장 큰 차이'

result = 0;

if(C==2): # 집이 두개라면, 무조건 처음집과 마지막집 사이의 거리
    print(house[N-1] - house[0]);  
else:
    while( start < end ): # 1 < 4이니까 한바퀴 더
        mid = ( start + end ) // 2; # 최소거리 + 최대거리 / 2 = 공유기설치 간격의 초기값 # 4 # 2
        count = 1; # 순회를 하면서 공유기 설치를 count 해야하므로 1로 초기화 해줘야 함.
        ts = house[0]; #공유기는 처음 집에 무조건 설치해야함 초기값 설정 # 1
        for i in range(N):
            if house[i] - ts >=mid:
                count+=1 #공유기설치 #2
                ts = house[i] #마지막으로 공유기설치한곳 업데이트 # 8
        if count >= C: #공유기의 간격 좁히기
            result = mid    
            start = mid +1 
        elif count < C:
            end = mid # 공유기의 간격을 줄이기 end = 4
    print(result)

#  /**
            # *  [ 효율성 ]
            # *  - 메모리: 38984KB
            # *  - 시간 : 504ms
        #    */
	