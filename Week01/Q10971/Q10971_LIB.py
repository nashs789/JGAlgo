import sys

N = int(sys.stdin.readline())
min_value = sys.maxsize
visited = [False] * N
cost_arr = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))

    for j in range(N):
        cost_arr[i][j] = inp[j]


def backTracking(curCity, cityCnt, total):
    global min_value

    if cityCnt == N:
        if cost_arr[curCity][0] != 0:
            min_value = min(min_value, total + cost_arr[curCity][0])
        return
    
    for idx in range(1, N):
        if not visited[idx] and cost_arr[curCity][idx] != 0:
            visited[idx] = True
            backTracking(idx, cityCnt + 1, total + cost_arr[curCity][idx])
            visited[idx] = False


backTracking(0, 1, 0)
print(min_value)