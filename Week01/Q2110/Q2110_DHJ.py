import sys
N, C = map(int, sys.stdin.readline().split())
home = []
for i in range(N):
    home.append(int(sys.stdin.readline()))
home.sort()

#이진탐색으로 파악해야 할 것: 인덱스가 아닌 '거리'
start = 1 #이진탐색의 시작지점 (가능한 최소거리)
end = home[-1] - home[0] #이진탐색의 끝지점 (가능한 최대거리)
result = 0

while start <= end:
    mid = (start + end) // 2 #중간값 = router를 설치하기 위해 벌려야 하는 최소한의 거리 
    count = 1
    router = home[0] #0번 인덱스의 집에 설치함

    for i in range(1, N):
        if home[i] - router >= mid: #가장 최근에 설치한 집에서부터 다음 라우터까지의 거리가 중간값보다 큰가?
            count += 1 #크다면 설치 후 
            router = home[i] #가장 최근에 설치한 집의 index를 갱신
    if count >= C: #주어진 공유기를 전부 설치했다면
        result = mid #최소한의 거리를 result로 담고
        start = mid + 1#가능한 최소한의 거리를 mid + 1로 갱신
        mid = (start + end) // 2
    elif count < C : #주어진 공유기를 전부 설치하지 못했다면
        end = mid - 1 #가능한 최대 거리를 mid로 줄임
        mid = (start + end) // 2

print(result)       