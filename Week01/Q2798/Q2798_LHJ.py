import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

def backtrack(cardIdx, combIdx):
    global blackJack
    if combIdx == 3:
        sumNum = sum(combLst)
        if sumNum <= M and sumNum > blackJack :
            blackJack = sumNum
            return
        return
    
    for i in range(cardIdx, N):
        if visited[i]: continue
        combLst[ combIdx ] = cards[ i ]
        visited[i] = True
        backtrack(cardIdx+1, combIdx+1)
        visited[i] = False

visited = [False]*N
combLst = [0]*3
blackJack = 0
backtrack(0, 0)
print(blackJack)