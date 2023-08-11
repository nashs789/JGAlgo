T = int(input())
for i in range(T):
    score = 0
    count = 0
    OX = input()
    for j in range(len(OX)):
        if OX[j] == 'O':
          count += 1
          score += count
        else:
           count = 0
    print(score)

#조건이 맞을 경우 count 를 1씩 증가시키고 증가시킨 만큼 score에 더하는 방법

# count = count + 1 을 count += 1 로 쓸 수 있음
        