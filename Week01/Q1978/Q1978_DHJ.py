N = int(input())
num_list = list(input().split())
num_list = list(map(int,num_list)) #숫자 배열
count = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in num_list:
    if is_prime(i):
        count += 1

print(count)
    

                