import sys
import itertools


givenNum = int(sys.stdin.readline())

givenNumList = list(map(str,sys.stdin.readline().split()))

givenOperatorNum = list(map(int,sys.stdin.readline().split()))

def makeStrOperList(List) : #모든 연산자 리스트에 넣기.
    tmpList = []
    tmpList.append('+' * List[0])
    tmpList.append('-' * List[1])
    tmpList.append('*' * List[2])
    tmpList.append('/' * List[3])

    return tmpList

tmpOperatorList = makeStrOperList(givenOperatorNum) # 갯수가 담긴 리스트를 makeStOperList메서드로 연산자 나열 리스트를 만들어 tmpOperatorList로 저장.

operList = list(char for string in tmpOperatorList for char in string) # tmpOperatorList를 연산자 각각마다 인덱싱

nCr = list(set(itertools.permutations(operList, givenNum-1))) 
# 각각마다 인덱싱 된 연산자리스트중 입력받은 수(givenNum)보다 -1개 만큼으로 순열을 나열하고, 
# 중복을 삭제 후 리스트변환(튜플으로 리턴받았은후 set형태로 리턴받았으므로)
# (N개의 수를 입력 받있다면 연산자는 N-1개 들어가기 때문)

def whatOperator(Operator, calcNum1) :
    if Operator == '+' :
        return '+' + calcNum1
    elif Operator == '-' :
        return '-' + calcNum1
    elif Operator == '*' :
        return '*' + calcNum1
    elif Operator == '/' :
        return '/' + calcNum1

tmpResultList = []
for i in nCr :
    tmp = givenNumList[0]
    for j in range(len(givenNumList)-1) :
        tmp = int(eval(tmp + whatOperator(i[j], givenNumList[j+1])))
        tmp = str(tmp)
    tmpResultList.append(tmp)

tmpResultListToInt = []
for s in tmpResultList:
    if '.' in s:
        tmpResultListToInt.append(int(float(s)))
    else:
        tmpResultListToInt.append(int(s))
tmpResultListToInt.sort() # 마지막 결과값을 sort하여 가장큰값, 가장작은값을 가져올 생각

print(tmpResultListToInt[-1])
print(tmpResultListToInt[0])
    
    

        


