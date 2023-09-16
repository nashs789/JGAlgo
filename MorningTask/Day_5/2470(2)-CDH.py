import sys
input = sys.stdin.readline;

N = int(input());
potions = [(map(int, input().split() )) for _ in range(N)]

# start ,end, middle, 종료조건
# middle값을 우째야하노..
potions.sort(); # [-99 -2 -1 4 98]
start , end = 0, len(potions) -1 ; # 인덱스로 가야되나 ..
result = 0;
while(start < end): # 0,4
    if(potions[start] + potions[end] < result): # 최소값이다.
        result = potions[start] + potions[end]; # result 갱신.. 그 이후는요 ?'
        start +=1;
    elif(start + end > result):
        end -=1;

print(potions[start], potions[end]);        
