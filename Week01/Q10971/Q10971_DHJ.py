import sys
N = int(sys.stdin.readline())
matrix_list = []
for i in range(N):
    matrix = list(map(int, sys.stdin.readline().split()))
    #행렬을 담은 이중 리스트
    matrix_list.append(matrix)

city_list = list(range(N))
visited = [0] * N
possible_route = [0] * N
minimum = sys.maxsize

#경로 구하기 순열
def perm(n, k):

    if n == k:
        circle_list = []
        total_cost = 0

        #실현가능한 모든 도시 경로 
        circle_list = possible_route
        #순회루트이므로 처음에 왔던 도시 추가
        circle_list.append(possible_route[0])

        global minimum
        for i in range(0, len(circle_list) - 1):

            cost = matrix_list[circle_list[i]][circle_list[i+1]]
            if cost == 0: 
                continue
            total_cost = total_cost + cost

        minimum = min(minimum, total_cost)

    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_route[k] = city_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False

perm(N, 0)

print(minimum)