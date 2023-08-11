num = []
for _ in range(9):
    n = int(input())
    num.append(n)

max_num = max(num)
print(max_num)

max_idx = num.index(max_num)
print(max_idx+1)