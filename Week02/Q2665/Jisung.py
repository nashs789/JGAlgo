import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 생각한 방법
# 1. bfs를 통해 주변 노드들다 조사함
# 2. 그때 끝방과 가장 가까운 부분을 찾음
# 3. 가까운 부분의 주변 1을 찾고, 그친구를 일단 열어봄
# 4. 그 후 다시 bfsf를 하고 또 가장 가까운 부분을 찾음
# 5. 마지막에 연결함
# 6. 각각의 방법으로 도착했을 때 가장 작게 연걸 기준으로 프린트함
#=======================================30분 초과
# 답지
# 1. bfs특성으로 일단 다 퍼트려
# 2. 짜피 도착했을때 경로가 최단이니까 그 경로에서 a에 몇개가 추가되었는지 확인하면 끝임
def Dijkstra():
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = []
    hq.heappush(q,(0,0,0))
    visited[0][0] = 1
    while q:
        a,x,y = hq.heappop(q)
        if x== N - 1 and y== N - 1:                                     # 끝에가서 print()해줌
            print(a)
            return
        for i in range(4):                                              # 네방향으로 1씩 이동하며 첫번째 if문에 위배되는지 확인하여 장외인지를 판별함
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:    # 장외 판별
                visited[nx][ny] = 1                                     # 아니라면 일단 visited에 1를 넣음, 어디까지 확산되었는지 확인하는 용도가 맞다.
                if graph[nx][ny] == 0:                                  # graph에서 못가는 곳을 만났을 때 일단 길을 내서 간다.
                    hq.heappush(q, [a + 1, nx, ny])                     # 만약 막힌길이라면 일단 뚫고 뻗어나간다.
                else:
                    hq.heappush(q, [a, nx, ny])                         # 딱히 막힌길이 아니더라도 일단 뻗어나간다.

Dijkstra()

