import sys
input = sys.stdin.readline

key =[]
for i in range(9):
    height = int(input())
    key.append(height)
key.sort()
sum = sum(key)

for i in range(8):
    for j in range(i+1,9):
        if sum-(key[i]+key[j])==100:
            for k in range(9):
                if k ==i or k ==j:
                    pass
                else:
                    print(key[k])
            exit()