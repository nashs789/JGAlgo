import sys
N = int(sys.stdin.readline())
matrix_list = []
for i in range(N):
    matrix = list(map(int, sys.stdin.readline().split()))
    #행렬을 담은 이중 리스트
    matrix_list.append(matrix)

city_list = list(range(N))
visited = [0] * N
#possible_route = [0] * N
minimum = sys.maxsize

#경로 구하기 순열
def perm(node, x, cost):
    global minimum
    if x == N:
        if matrix_list[node][0]: #2. 이 부분 역시 마지막 node에서 출발점으로 돌아가는 경로가 0은 아닌지 판정
            minimum = min(minimum, cost + matrix_list[node][0])
        return


    for next_node in range(1, N):
        if matrix_list[node][next_node] and not visited[next_node]: #1. 시간초과가 나지 않으려면, 값이 0인 경로를 이용하는 루트를 애초에 짜야함
            visited[next_node] = True
            perm(next_node, x+1, cost+matrix_list[node][next_node])
            visited[next_node] = False

perm(0, 1, 0)

print(minimum)