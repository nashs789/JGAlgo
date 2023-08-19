import sys

givenStringList = str(sys.stdin.readline().strip())

stringList = list() # (()[[]])([])

for i in givenStringList :
    stringList.append(i)

tmpX = 0
tmpY = 0

tmp = 1
result = 0

tmp2 = 0
tmp3 = 0
while True :
    if tmpX > 0 or tmpY > 0 :
        result = 0
        break
    elif len(stringList) == 0 :
        result = 0
        break
    
    if stringList[-1] == ')' :
        stringList.pop()
        tmpX -= 1
        if stringList[-1] != ')' :
            tmp2 -= 1
        
    elif stringList[-1] == '(' :
        stringList.pop()
        tmp *= 2
        tmpX += 1
        if len(stringList) != 0 and (stringList[-1] == ']' or stringList[-1] == ')') :
            tmp2 += 1                
            if tmp2 == 0 :
                tmp *= 2
            result += tmp
            tmp = 1
            
    elif stringList[-1] == ']' :
        stringList.pop()
        tmpY -= 1
        if stringList[-1] != ']' :
            tmp3 -= 1
        
        
    elif stringList[-1] == '[' :
        stringList.pop()
        tmp *= 3
        tmpY += 1
        if len(stringList) != 0 and (stringList[-1] == ')' or stringList[-1] == ']') :
            tmp3 += 1                
            if tmp3 == 0 :
                tmp *= 3
            result += tmp
            tmp = 1
    
    
    if len(stringList) == 0 and tmpX == 0 and tmpY == 0 :
        break
    
print(result)