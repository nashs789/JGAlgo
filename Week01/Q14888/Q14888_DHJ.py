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

possible_list = [0] * (len(num_list) - 1)
answer_list = []
def perm(n, k):
    if n == k:
        #가능한 리스트를 구하고 바로 결과를 계산하기
        temp_value = num_list[0]
        for i in range(0, len(possible_list)):
            if possible_list[i] == 'plus':
                temp_value = temp_value + num_list[i + 1]
            elif possible_list[i] == 'minus':
                temp_value = temp_value - num_list[i + 1]
            elif possible_list[i] == 'multiply':
                temp_value = temp_value * num_list[i + 1]
            else:
                if temp_value < 0:
                    temp_value = temp_value * -1
                    temp_value = (temp_value // num_list[i + 1]) * -1
                else:
                    temp_value = temp_value // num_list[i + 1]

        answer_list.append(temp_value)
            
    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_list[k] = operator_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False
    
perm(len(operator_list), 0)

print(max(answer_list))
print(min(answer_list))

#python으로 돌리면 시간 초과 함 pypy로 돌렸음
# print(possible_list_list)
# value_list = []
# for sub_list in possible_list_list:
#     print('1')
#     print(sub_list)
#     for operator in sub_list:
#         print('2')
#         print(operator)
#         temp_result = num_list[0]
#         print('3')
#         print(num_list)
#         if operator == 'plus':
#             temp_result = temp_result + num_list[1]
#             num_list.pop(0)
#             num_list.pop(1)
#             print(temp_result)
#         elif operator == 'minus':
#             temp_result = temp_result - num_list[1]
#             num_list.pop(0)
#             num_list.pop(1)
#             print(temp_result)
#         elif operator == 'multiply':
#             temp_result = temp_result * num_list[1]
#             num_list.pop(0)
#             num_list.pop(1)
#             print(temp_result)
#         elif operator == 'divide':
#             if temp_result < 0:
#                 temp_result = temp_result * -1
#             temp_result = (temp_result // num_list[1]) * -1
#             num_list.pop(0)
#             num_list.pop(1)
#             print(temp_result)


#         value_list.append(temp_result)

