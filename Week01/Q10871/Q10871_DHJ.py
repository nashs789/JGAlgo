
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    print(i)
    if i < X:
        print(i, end=" ")

    
#print의 옵션
#sep=" ": print 출력문들 사이에 해당하는 내용을 넣을 수 있음. 기본값은 공백
#end=" ": print물을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있음. 기본값은 개행(\n)
# for i in A 반복문에서 i는 배열 A의 원소를 의미한다.