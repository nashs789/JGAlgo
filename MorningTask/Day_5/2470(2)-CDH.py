import sys
import math
input = sys.stdin.readline;

N = int(input());
potions = list(map(int, input().split() ))

# start ,end, middle, 종료조건
# middle값을 우째야하노..
potions.sort(); # [-99 -2 -1 4 98]
start , end = 0, N -1 ; # 인덱스로 가야되나 ..
result = math.inf
resultArr = []

while(start < end): # 0,4
    sumsum = potions[start] + potions[end];
    if(abs(sumsum) < abs(result)):
        result = sumsum;
        resultArr = [potions[start], potions[end]];
    if(result == 0):
        result = sumsum;
        resultArr = [potions[start], potions[end]];
        break;
        
    if(sumsum < 0):
        start +=1;
    else:
        end-=1

print(resultArr[0], resultArr[1]);
