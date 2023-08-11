import sys
count = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))


def find_num(num):
    if num == 1:
        return 0
    for i in range(2, int(num/2)+1):
        if num % i != 0:
            continue
        else:
            return 0
    return 1

count = 0
for n in num: # 3, 15, 16
    count += find_num(n)
print(count)