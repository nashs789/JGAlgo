import sys

N = int(sys.stdin.readline())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()

for i in num_list:
    sys.stdout.write(str(i))

#1이랑 똑같은 풀이로 풀리긴 하는데 너무 오래걸림 메모리 77108 KB 시간 1512ms