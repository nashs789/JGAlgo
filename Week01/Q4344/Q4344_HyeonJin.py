n = int(input())

all_scores = []
for _ in range(n):
    nums = list(map(int, input().split()))
    all_scores.append(nums)

for score in all_scores:
    score.remove(score[0])
    score_avg = sum(score)/len(score)
    students = len(score)
    score = [ student for student in score if student > score_avg ]
    high = len(score)
    a = round((high/students*100), 3)
    print('%.3f'%a,'%')