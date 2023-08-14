import sys
N = int(sys.stdin.readline())
matrix_list = []
for i in range(N):
    matrix = list(map(int, sys.stdin.readline().split()))
    #행렬을 담은 이중 리스트
    matrix_list.append(matrix)

print(matrix_list)

city_list = []
for i in range(N):
    city_list.append(i)

print(city_list)

possible_route = [0] * N
possible_route_list = []
visited = [0] * N

#경로 구하기 순열
def perm(n, k):

    if n == k:
        new_list = []
        for i in possible_route:
            new_list.append(i)
        possible_route_list.append(new_list)


    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_route[k] = city_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False

perm(N, 0)

#실현가능한 모든 도시 경로 
possible_route_list.append(possible_route)

#순회루트이므로 처음에 왔던 도시 추가
for route in possible_route_list:
    route.append(route[0])

total_cost = []
total_cost_list = []
for route in possible_route_list:
    for i in range(0,len(route) - 1):
        cost = matrix_list[route[i]][route[i+1]]

        if cost == 0:
          pass

        total_cost.append(cost)

    sum_total_cost = sum(total_cost)
    total_cost_list.append(sum_total_cost)
    total_cost.clear()

print(min(total_cost_list))