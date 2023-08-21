import sys
sys.setrecursionlimit(10**6)

N, M = map(int,sys.stdin.readline().split())

givenList = [[] for _ in range(N+1)]

for i in range(M) :
    A, B = map(int,sys.stdin.readline().split())
    givenList[A].append(B)
    givenList[B].append(A)
    
def DFS(start) :
    visited[start] = True
    
    for i in givenList[start] :
        if visited[i] == False :
            visited[i] = True
            DFS(i)
    
visited = [False]*(N+1)

count = 0
for i in range(1, N+1) :
    if visited[i] == False :
        count += 1
        DFS(i)
print(count)