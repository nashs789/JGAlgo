# 에제는 다 맞는데 3%에서 틀림

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[False]*(N+1) for _ in range(N+1)]
for i in range(K):
    x,y = map(int, input().split())
    graph[x][y] = True
L = int(input())
change = deque([list(map(str,input().split())) for _ in range(L)])
snake = deque([[1,1]])


def Dummy(snake,N,change):

    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    di_num = 0
    sec = 0
    temp_x = 0
    temp_y = 0

    while snake[0][0]<=N and snake[0][1]<=N and snake[0][0]>0 and snake[0][1]>0:
        # 이동
        sec += 1
        temp_x = snake[0][0]
        temp_y = snake[0][1]
        temp_x += direction[di_num][0]
        temp_y += direction[di_num][1]
        # 자기몸이랑 겹치는지 확인
        if [temp_x,temp_y] in snake:
            return sec
        snake.appendleft([temp_x,temp_y])
        snake.pop()


        # 사과를 먹었을 때 한줄 늘리기
        if graph[temp_x][temp_y]==True:
            snake.append([temp_x,temp_y])
        
        # 회전
        if len(change)>0:
            if int(change[0][0])==sec:
                if change[0][1]=="D":
                    di_num += 1
                    di_num %= 4
                else:
                    di_num -= 1
                    di_num %= 4
                change.popleft()
    return sec

print(Dummy(snake,N,apple,change))

# 직진하다가 사과를 만나면 sanke에 중간저장후 위치변경, 중간저장한거 뒤에 저장하는식으로 만든다
# snake가 이동할때는 앞에 값을 뒤로 전달하는식으로 만든다. 큐를 여기서 사용
# 게임 끝내는법
# - snake[0]이 장외하는지 확인하기
# - snake[0]이 뒤에 꼬리와 겹치는지 확인