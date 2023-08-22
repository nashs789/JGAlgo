import sys
sys.setrecursionlimit(10**8)
import heapq as hq
input = sys.stdin.readline

# 크루스칼 알고리즘
# 1. 선택되지 않은 간선들 중 최소 가중치인 간선을 선택한다.
# 2. 만약 그 간선을 선택했을 때, 지금까지 구성된 스패닝 트리에 사이클이 없을 경우에만 선택한다.
    # 사이클 확인은 부모노드가 같은지를 통해 확인할 수 있다.
# 3. 총 V-1(정점의 개수 -1)개의 간선이 선택될 때까지 반복한다.

N,E = map(int,input().split())
total = []
for _ in range(N):
    s,e,w = map(int,input().split())
    hq.heappush(total,(w,s,e))

Vroot = [i for i in range(N+1)]    # 부모노드

def find(x):                       # 해당 정점에 대한 부모노드를 찾는 함수
    if x!= Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

result = 0
for s,e,w in total:
    sRoot = find(s)
    eRoot = find(e)               # 부모노드가 같을때 사이클이 생기므로 시작점과 끝점의 
    if sRoot != eRoot:            # 부모노드가 다를 때 성립하게 만든다.
        if sRoot > eRoot:         # 둘 중에 더 작은쪽의 부모노드로 통일한다.
            Vroot[sRoot] = eRoot  
        else:
            Vroot[eRoot] = sRoot
        result += w

print(result)