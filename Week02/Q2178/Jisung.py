# 답지보고 이해했어요
import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
graph = []

for _ in range(N):
	graph.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	q = deque()
	q.append((x,y))
	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
				q.append((nx,ny))
				graph[nx][ny] = graph[x][y] + 1
	return graph[N-1][M-1]

print(bfs(0,0))

# bfs를 사용함
# 초기값을 0,0에 넣어서 좌표 1,1에서 출발하도록 만듬
# for문을 통해 상하좌우를 확인한다.
# if문을 통해서 맵밖으로 나가는지 확인하고 이동한 해당자리에 1이 있는지 확인한다.
# 갈수 있는 모든 자리들을 확인하고 q에 넣어서 이동한다.
# 이동한 자리에는 이동하기 전보다 1을 더해 얼마만에 가는지 표시한다.
# 참조 - 길찾아갈때 왼쪽 오른쪽을 기준으로 하나식 더해서 길로 가는 모든 경로를 표시하는거랑 같다고 생각하면 될듯