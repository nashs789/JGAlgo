# 에제는 다 맞는데 3%에서 틀림

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
apple = [list(map(int,input().split())) for x in range(K)]
apple.sort()
L = int(input())
change = deque([list(map(str,input().split())) for y in range(L)])
snake = deque([[1,1],[1,1]])


def Dummy(snake,N,apple,change):

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
        snake.appendleft([temp_x,temp_y])
        # 자기몸이랑 겹치는지 확인
        for i in range(1,len(snake)):
            if temp_x==snake[i][0] and temp_y==snake[i][1]:
                return sec
        snake.pop()


        # 사과를 먹었을 때 한줄 늘리기
        if len(apple)>0:
            if snake[0]==apple[0]:
                apple.pop(0)
                snake.append(snake[-1])
        
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
