import sys

input=sys.stdin.readline

sick=input().split('-') #split 안쓰게되면 공백을 기분으로 구분

num = [] # '-'로 구분한 항들의 합을 저장할 리스트

for i in sick:
    sum=0 # 각 항마다 새로운 합계를 계산하기 위해, 밖에다가 쓰면 첫번째항의 결과가 다음항에 영향을 미치기떄문에
    plus = i.split('+') #덧셈을 하기 위해 '+'기준으로 구분
    for j in plus:# 구분한 리스트의 각 요소 플러스
        sum+=int(j)
    num.append(sum)#각 항의 연산 결과를 num에 저장

n=num[0] #식의 제일 처음은 숫자로 시작하기 떄문에 0번째 값에서 나머지 값 뻄

for i in range(1,len(num)):#1부터 n에서 빼줌
    n-=num[i]
print(n)


