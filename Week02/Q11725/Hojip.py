import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

givenList = [[] for _ in range(N+1)] # N+1로(8) 하는게 맞음.
visited = [False] * (N+1)
par = [0] * (N+1)

for i in range(N-1) :
    A, B = map(int,sys.stdin.readline().split())
    givenList[A].append(B)
    givenList[B].append(A) # 양방향 노드 트리 선언
    

def DFS(start) :
    visited[start] = True
    
    for i in givenList[start] :
        if visited[i] == False :
            par[i] = start
            DFS(i)
        

DFS(1)

for i in range(2, len(par)) :
    print(par[i])

