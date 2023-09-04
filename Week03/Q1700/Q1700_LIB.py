N, K = map(int,input().split(' '))
use = list(map(int,input().split(' ')))
code = []
answer = 0

for this in range(K):
    print(this)
    if use[this] in code :  # 코드에 이미 꽂혀져있음
        continue

    if len(code) < N :  # 코드 자리 남음
        code.append(use[this])
        continue

    priority = []
    for c in code:  # 꽂혀져 있는 코드들
        if c in use[this:]: # 다음에 또 이용해야한다면
            priority.append(use[this:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(use[this])
    answer += 1

print(answer)