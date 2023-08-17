import sys
M, N, L = map(int, sys.stdin.readline().split())

gun = list(map(int, sys.stdin.readline().split()))
gun.sort()
animal = []
for i in range(N):
    animal.append(list(map(int, sys.stdin.readline().split())))

count = 0
for x, y in animal:
    if y > L:
        continue
    gun_min = x + y - L
    gun_max = x - y + L
    start = 0
    end = M - 1
    while start <= end:
        mid = (start + end) // 2
        if gun[mid] >= gun_min and gun[mid] <= gun_max:
            count += 1
            break
        elif gun[mid] < gun_max:
            start = mid + 1
        else:
            end = mid - 1

print(count)


#사대를 기준으로 잡을 수 있는 동물을 구하려고 하면 시간 복잡도가 높아짐
#동물을 기준으로 잡을 수 있는 사대가 존재하는지를 구하는 것이 더 빠름
#동물의 위치 (x,y)를 기준으로, 잡을 수 있는 사대의 좌표는 최소 x + y - l, 최대 x - y + l
#이진탐색의 기준점을 start, end 로 지정 후, start <= end 인 동안 (최소좌표) x + y - l <= mid <= x -y + l (최대좌표) 인지 확인한다.
#물론 y 가 l 보다 크면 애초에 잡을 수 없으므로 조기 종료
#해당 구간에 mid가 존재한다면 count + 1 후 반복문 탈출
#mid 가 최소값보다 작다면 start = mid + 1
#mid 가 최소값보다 크다면 end = mid - 1
