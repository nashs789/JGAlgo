import sys

givenNum = int(sys.stdin.readline())

tmp = list()
for i in range(givenNum) :
    tmp.append(list(map(str,sys.stdin.readline().strip())))

for i in tmp :
    tmpValue = 0
    while True :

        if i.pop() == ")" :
            tmpValue -= 1
        else :
            tmpValue += 1
        
        if tmpValue > 0 :
            print("NO")
            break
        elif len(i) == 0 and tmpValue == 0  :
            print("YES")
            break
        elif len(i) == 0 and tmpValue < 0 :
            print("NO")
            break
        else :
            continue
            

