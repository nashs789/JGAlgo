import sys

Num = int(sys.stdin.readline())

givenList = list()

for i in range(Num) :
    givenList.append(list(map(str,sys.stdin.readline().split())))


resultList = list()

for i in givenList :
    if i[0] == "push" :
        resultList.append(i[1])
    elif i[0] == "top" :
        if len(resultList) != 0 :
            print(resultList[-1])
        else :
            print(-1)
    elif i[0] == "size" :
        print(len(resultList))
    elif i[0] == "empty" :
        if len(resultList) == 0 :
            print(1)
        else :
            print(0)
    elif i[0] == "pop" :
        if len(resultList) != 0 :
            print(resultList.pop())
        else :
            print(-1)