A = int(input())
B = int(input())
C = int(input())

result = A * B * C
str_result = str(result)
for num in range(1):
    list_num = list(map(int, str_result))

for i in range(0,10):
    count = 0
    for j in list_num:
        if j == i:
            count += 1
    print(count)
