C = int(input())
for i in range(C):
    grade_list = list(input().split(" "))
    num = int(grade_list[0]) #학생수를 분리
    grade_list.pop(0)
    grade_list = list(map(int, grade_list)) #정수 타입 배열로 변경
    average = sum(grade_list) / num #평균값
    count = 0
    for grade in grade_list:
        if grade > average:
            count += 1
    percentage = count / num * 100
    print(f'{percentage:.3f}%') #소숫점 아래 3자리까지 표시

    #파이썬에서 소수 몇 자리까지 표시할 것인가 형식