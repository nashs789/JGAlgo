num = int(input())

for idx in range(0, num):
    answer = input()
    score = 0
    seq = 1

    for s in answer:
        if s == 'O':
            score += seq
            seq += 1
        else:
            seq = 1
    print(score)