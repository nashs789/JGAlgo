import sys
a, b = map(list, sys.stdin.readline().split())

a.reverse()
b.reverse()
for i in range(3):
    if a[i] > b[i]:
        print(a[0]+a[1]+a[2])
        break
    elif a[i] < b[i]:
        print(b[0]+b[1]+b[2])
        break
    else:
        continue

# 방법2
a, b = sys.stdin.readline().split()
a = int(a[::-1])
b = int(b[::-1])

print(a) if a > b else print(b)