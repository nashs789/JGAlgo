import sys

N, K = map(int,sys.stdin.readline().split())
givenNum = int(sys.stdin.readline())
givenNumList = list(map(int, str(givenNum)))


stack = []
stack.append(givenNumList.pop())
maxNum = int()
for i in range(N) :
    while True :
        