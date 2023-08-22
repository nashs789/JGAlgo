import sys
from collections import deque

K = int(sys.stdin.readline())
answer = [False] * K

def BFS(start) :
    q = deque()
    q.append(start)
    visited[start] = True
    tmpWhiteBlack[start] = 1
    while q :
        cur = q.popleft()
        for i in givenList[cur] :
            if not visited[i] :
                visited[i] = True
                tmpWhiteBlack[i] = -tmpWhiteBlack[cur]
                q.append(i)
            elif tmpWhiteBlack[i] == tmpWhiteBlack[cur] : # 같은 그룹에 속하면
                return False
    return True


for _ in range(K) :
    V, E = map(int,sys.stdin.readline().split())
    givenList = [[] for _ in range(V+1)]
    for _ in range(E) :
        a, b = map(int,sys.stdin.readline().split())
        givenList[a].append(b)
        givenList[b].append(a)
        # [[][3][3]]
    tmpWhiteBlack = [0] * (V+1)
    visited = [False] * (V+1)
    
    result = "YES"
    for j in range(1, V+1) :
        if not visited[j] and not BFS(j) :
            result = "NO"
            break
    
    print(result)
