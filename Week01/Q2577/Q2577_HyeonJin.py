a = int(input())
b = int(input())
c = int(input())

value = str(a * b * c)

# 방법1
count = 0
for i in range(10):
    for v in value:
        if int(v) == i:
            count+=1
    print(count)
    count = 0


# 방법2
count = [0]*10

for v in value:
    count[int(v)]+=1

for r in count:
    print(r)