import sys

N, K = map(int,sys.stdin.readline().split())
givenNum = int(sys.stdin.readline())
givenNumList = list(map(int, str(givenNum)))


stack = []
stack.append(givenNumList.pop())
maxNum = int()
for i in range(N) :
    while True :
        if len(givenNumList) == 0 :
            break
        if stack[-1] > givenNumList[-1] : # 4 < 2라면
            givenNumList.pop()
        else :
            stack.pop()
            stack.append(givenNumList.pop())
            K -= 1