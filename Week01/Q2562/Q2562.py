maxV = 0
maxIdx = 0

for idx in range(1, 10):
    num = int(input())
    
    if maxV < num:
        maxV = num
        maxIdx = idx

print(maxV)
print(maxIdx)