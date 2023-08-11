A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
arr = [0] * 10

for s in result:
    arr[int(s)] += 1

for idx in arr:
    print(idx)