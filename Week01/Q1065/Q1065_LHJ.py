import sys
num = int(sys.stdin.readline())

# 1 보다 크고 N보다 작은 한수의 개수 출력!
result = 0
for i in range(1, num+1):
    if i<100:
        result += 1
    elif i < 1000:
        if (i%10 - i//10%10 == i//10%10-i//100):
            result+=1

print(result)