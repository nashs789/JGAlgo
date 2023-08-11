cnt, target = map(int, input().split())

def func(n):
    return n < target

numArr = list(map(int, input().split()))
result = list(filter(func, numArr))

for item in result:
    print(item, end=' ');