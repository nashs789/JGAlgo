num = int(input())

qz = []
for _ in range(num):
    a = input()
    qz.append(a)

score = 0
plus = 1

for n in range(num):
    for q in qz[n]:
        if q == 'O':
            score += plus
            plus+=1
        else:
            plus = 1
    print(score)
    score = 0
    plus = 1