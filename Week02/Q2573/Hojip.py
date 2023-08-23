import sys
from collections import deque
#1. BFS를 반복문 처음에 돌려서 빙산의 갯수가 몇인지 찾기 => 2이상이면 빙산의 갯수를 출력하고 break
#2. 이중for문을 돌려서 첫번째 점을 찾는다. 이 때 이중포문 돌기 전 맨처음에 #1의 방법을 사용하여 빙산의 갯수가 몇개인지부터 돌게한다.
#3. 이중for문을 돌려서 첫번째 점을 찾았으면 BFS를 돌려서 상하좌우 0의 갯수에따라 해당노드를 감소시키고 0이 되면 -1을 준다(먼저 0이되게해버리면 다른 노드에 영향을 줌.)
#4. 마지막에 -1과 숫자로 이루어진 빙산을 토대로, -1을 0으로 되돌려준다.
#5. 만약 첫번째 BFS를 돌렸는데 0이 나온다면 그대로 0을 출력한다.

# TODO : 마지막으로, BFS를 돌려서 빙산의 갯수가 몇인지 찾는것을 구현하여야함.

N, M = map(int,sys.stdin.readline().split())

givenList= []

for _ in range(N) :
    givenList.append(list(map(int,sys.stdin.readline().split())))


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def BFS2(y, x) : # 빙산과 만나는 첫 지점 y, x이고, 빙산의 주변에 물이 있다면 감싸지는 빙산이 면적에따라 -되는 BFS임.
    q = deque()
    q.append((y, x))
    isVisited[y][x] = True
    while q :
        y1, x1 = q.popleft()
        for dy, dx in d :
            if 0 <= dy+y1 < N and 0 <= dx+x1 < M :
                if givenList[dy+y1][dx+x1] == 0 :
                    givenList[y1][x1] -= 1
                    if givenList[y1][x1] <= 0 :
                        givenList[y1][x1] = -1 # 연산 중간에 빙산의 값이 0에 닿는다면 -1을 넣어줌.
                        continue
                elif givenList[dy+y1][dx+x1] > 0 and isVisited[dy+y1][dx+x1] == False:
                    q.append((dy+y1,dx+x1))
                    isVisited[dy+y1][dx+x1] = True
                    
    for i in range(N) :
        for j in range(M) :
            if givenList[i][j] == -1 :
                givenList[i][j] = 0


while True :
    
    Y = int()
    X = int()
    isFound = False
    for i in range(N) :
        for j in range(M) :
            if givenList[i][j] != 0 : # 첫 점 찾기.
                Y = i
                X = j
                isFound = True
                break
        if isFound :
            break

    isVisited = [[False for _ in range(M)] for _ in range(N)]

    BFS2(Y, X)




for i in givenList :
    print(i)