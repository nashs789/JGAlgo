import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
givenList = [[] for _ in range(N+1)]
numChild = [0] * (N+1)

answerList = [[0 for _ in range(N+1)]for _ in range(N+1)]


for i in range(M) :
    A, B, C = map(int,sys.stdin.readline().split())
    givenList[B].append((A,C))
    numChild[A] += 1

List = []
q = deque()
for i in range(1, N+1) :
    if numChild[i] == 0 :
        answerList[i][i] = 1
        q.append(i)
        List.append(i)

while q :
    cur = q.popleft()
    
    for Next,Cost in givenList[cur] :
        for i in range(1, N+1) :
            answerList[Next][i] += answerList[cur][i] * Cost
        numChild[Next] -= 1
        if numChild[Next] == 0 :
            q.append(Next)

    
for i in List :
    print(i, answerList[N][i])