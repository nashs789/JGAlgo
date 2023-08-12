#한수: 1의 자리, 2의자리의 모든 양의 정수는 한수로 취급

def hansu(n):
    if n <= 99:
        return True
    elif n == 1000:
        return False
    else:
        num_list = list(map(int, str(n))) 
        #int 타입 데이터는 map으로 나눌 수 없으므로 str로 변환한 다음 map 메소드로 int로 선언하여 리스트에 넣었음
        if num_list[2] - num_list[1] == num_list[1] - num_list[0]: #각 자리수 간 차이 비교
            return True
        else:
            return False
        
N = int(input())
count = 0
for i in range(1,N+1):
    if hansu(i):
        count += 1
print(count)
        
  
    