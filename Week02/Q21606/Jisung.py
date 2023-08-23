import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
is_inside = [0] + list(map(int,input().strip()))
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
count = 0
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    # 둘다 실내일때
    if is_inside[x]==1 and is_inside[y]==1:
        count += 2

# 접근방식
# 1. 실외에서 시작해서 temp에 1씩 넣어주고 dfs를 통해 노드의 끝부분에서 2가 되면 count를 세준다.
#-----------------------30분 시간초과

# 블로그참조 문제접근(https://velog.io/@tmdejr1117/SW%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-%EC%A0%95%EA%B8%8023%EC%9D%BC%EC%B0%A8-TIL-%EB%B0%B1%EC%A4%80-21606-%EC%95%84%EC%B9%A8-%EC%82%B0%EC%B1%85%ED%8C%8C%EC%9D%B4%EC%8D%AC)
# 1. 실외노드가 아닌 실내 노드를 기준으로 인접한 노드 실내노드를 세는것이 더 좋다
# 2. 실외 노드를 가운데로 놓고 인접한 실내 점n개가 붙어있을 때, 갈 수 있는 경로의 수는 n(n-1)이 된다.
# -> 먼저 실내의 점 1개를 고르고, 그 이후 남은 실내의 점을 고르는 경우의 수이므로 n(n-1)이 된다.
# 3. for문을 돌면서 실외 점을 만났을 때 해당 점을 아직 방문하지 않았다면 그 점을 기준으로 dfs재귀를 돌린다.
#-----------------------30분 구현실패

# 추가로 생각해야할 케이스
# 1. 실외 사이에 실내가 껴있는 경우
    # 중간에 실내가 껴있을 때는 재귀를 통해 순회할 수 있도록 만든다.
# 2. 주어진 두 점이 실내인 경우
    # 실내실내이므로 +2해준다.


def dfs(v,cnt):
    visited[v] = True
    for i in graph[v]:
        if is_inside[i]==1:	# 해당 노드의 위치가 실내이면
            cnt += 1		# 실내 개수 카운트에 +1 해준다.
        elif not visited[i] and is_inside[i] == 0:		# 방문하지 않았고 해당 i점의 위치가 실외라면.
            cnt = dfs(i,cnt)			# 해당 실외점을 기준으로 dfs를 돈다.
    return cnt


sums = 0
for j in range(1,N+1):
    if is_inside[j]==0 and not visited[j]:	# 실외를 기준으로
        x = dfs(j,0)				# 현재 cnt는 0
        sums += x*(x-1)				# 실외인 노드를 기준으로 면접 노드 애들 개수 세는 것이 n*(n-1)이므로 실외 노드 걸릴때마다 전부 세기
print(count+sums)
