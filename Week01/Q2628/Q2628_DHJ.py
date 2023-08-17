H, V = map(int, input().split())
L = int(input())
H_list = [0, H]
V_list = [0, V]
for i in range(0, L):
    measure, point = map(int, input().split())
    if measure == 1:
      H_list.append(point)
    else:
      V_list.append(point)
H_list.sort()
V_list.sort()

minus_H_list = []
minus_V_list = []
for i in range(1, len(H_list)):
   minus_H_list.append(H_list[i] - H_list[i-1])
for i in range(1, len(V_list)):
   minus_V_list.append(V_list[i] - V_list[i-1])

print(max(minus_H_list) * max(minus_V_list))

#알고리즘 관련 문제가 아니라 가로줄을 그으면 세로 축에 접점이 생긴다는 당연한 사실을 모르고 Horizon 과 Vertical 을 바꿔서 계산하는 삽질을 했다.