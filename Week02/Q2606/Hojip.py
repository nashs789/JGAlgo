import sys
sys.setrecursionlimit(10**6)

ComputerNum = int(sys.stdin.readline())

numberPair = int(sys.stdin.readline())

List = [[] for _ in range(ComputerNum+1)]

for _ in range(numberPair) :
    A, B = map(int,sys.stdin.readline().split())
    List[A].append(B)
    List[B].append(A)

count = 0
def DFS(start) :
    global count
    visited[start] = True
    for i in List[start] :
        if visited[i] == False :
            visited[i] = True
            count += 1
            DFS(i)
    

visited = [False]*(ComputerNum+1)
DFS(1)

print(count)