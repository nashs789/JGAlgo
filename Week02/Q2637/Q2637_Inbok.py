import sys
from collections import deque

def topology_sort():
    while queue:
        cur_node = queue.popleft()    # 현재 노드 번호

        # linked_node: 간선이 연결된 노드 번호, pieces: 연결된 노드를 만들기 위해 필요한 부품의 개수
        for linked_node, pieces in adj[cur_node]:
            indegree[linked_node] -= 1    # 연결된 노드 진입 차수 -1 (간선을 끊어주는 개념)

            # parts 에 아무것도 들어있지 않은 경우
            # ex) 5번 노드는 처음에 아무것도 들어있지 않아서 1번 2개, 2번 2개 {1: 2, 2: 2} 이런 식으로 값을 채움
            if len(parts[cur_node]) == 0:
                parts[linked_node][cur_node] = pieces
            else:
                # parts에 현재 노드를 만드는데 필요한 기존 노드에 대한 정보가 있는 경우 기존 노드 번호를 꺼낸다.
                # 기존 노드가 몇 개 필요한지 그리고 다음 노드를 만드는데 현재 노드가 얼마나 필요한지 계산
                # ex) 7번 노드는 5번 노드가 2개 필요하고, 5번 노드는 {1: 2, 2: 2}가 기록되어 있기 때문에
                # 7번 노드에는 {1: 4, 2: 4}로 기록 되어진다.
                # if ~ else 분기: dictionary에 key가 있는 경우와 없는 경우
                for key in parts[cur_node]:
                    if key in parts[linked_node]:
                        parts[linked_node][key] += parts[cur_node][key] * pieces
                    else:
                        parts[linked_node][key] = parts[cur_node][key] * pieces

            if indegree[linked_node] == 0:
                queue.append(linked_node)

if __name__ == "__main__":
    input = sys.stdin.readline
    queue = deque()
    N = int(input())
    M = int(input())

    parts = [{} for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        X, Y, K = map(int, input().split())

        adj[Y].append((X, K))    # 출발지가 Y 목적지가 X인 단방향 그래프
        indegree[X] += 1         # 진입 차수 +1

    for node in range(1, N):
        if indegree[node] == 0:  # 진입차수가 0인 노드만 queue에 넣고 시작
            queue.append(node)

    topology_sort()    # 위상정렬 시작

    for key in sorted(parts[N].keys()):
        print(key, parts[N][key])