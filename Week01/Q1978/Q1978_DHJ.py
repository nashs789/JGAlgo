N = int(input())
num_list = list(input().split())
num_list = list(map(int,num_list)) #숫자 배열
count = 0
for i in num_list:
    for j in range(2, i):
        if i % j != 0:
            pass
        else:
            break
    count += 1

print(count)
print(1 % 2)
    

                