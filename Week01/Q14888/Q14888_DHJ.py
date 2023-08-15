import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
plus, minus, multiply, divide = map(int, sys.stdin.readline().split())
operator_list = []
visited = [False] * (len(num_list) - 1)

for _ in range(plus):
    operator_list.append('plus')
for _ in range(minus):
    operator_list.append('minus')
for _ in range(multiply):
    operator_list.append('multiply')
for _ in range(divide):
    operator_list.append('divide')
print(operator_list)
possible_list = [0] * (len(num_list) - 1)
possible_list_list = []
def perm(n, k):
    if n == k:
        print(possible_list)
        temp = possible_list.copy() #여기서 temp에 현재의 possible_list 값을 복사하지 않으면 list_list에는 마지막에 생성된 list가 여러번 들어가게 된다
        possible_list_list.append(temp)

    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_list[k] = operator_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False
    
perm(len(operator_list), 0)

print(possible_list_list)
value_list = []
for sub_list in possible_list_list:
    print('1')
    print(sub_list)
    for operator in sub_list:
        print('2')
        print(operator)
        temp_result = num_list[0]
        print('3')
        print(num_list)
        if operator == 'plus':
            temp_result = temp_result + num_list[1]
            num_list.pop(0)
            num_list.pop(1)
            print(temp_result)
        elif operator == 'minus':
            temp_result = temp_result - num_list[1]
            num_list.pop(0)
            num_list.pop(1)
            print(temp_result)
        elif operator == 'multiply':
            temp_result = temp_result * num_list[1]
            num_list.pop(0)
            num_list.pop(1)
            print(temp_result)
        elif operator == 'divide':
            if temp_result < 0:
                temp_result = temp_result * -1
            temp_result = (temp_result // num_list[1]) * -1
            num_list.pop(0)
            num_list.pop(1)
            print(temp_result)


        value_list.append(temp_result)

print(value_list)