C = int(input())
for i in range(C):
    grade_list = list(input().split(" "))
    num = int(grade_list[0]) #학생수를 분리
    grade_list.pop(0)
    grade_list = list(map(int, grade_list)) #정수 타입 배열로 변경
    average = sum(grade_list) / num #평균값
    print(average)
    for i in grade_list:
        count = 0
        if i > average:
            count += 1
    print(count)