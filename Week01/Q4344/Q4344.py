cnt = int(input())

for i in range(0, cnt):
    inp = list(map(int, input().split()));
    inp[0] += 1
    sum = 0
    
    for j in range(1, inp[0]):
        sum += inp[j]
    
    avg = sum / (len(inp) - 1)
    overAvg = 0

    for j in range(1, inp[0]):
        if avg < inp[j]:
            overAvg += 1

    print(format(round(overAvg / (inp[0] - 1) * 100, 3), ".3f"),"%")