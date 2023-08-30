n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 끝나는 시간으로 sorting # x는 튜플 자료. (s, e)를 바꾼다.
# 정렬하는 key의 기준 : x[1](시작타임)-우선순위 / x[0](끝나는타임)-차순위
meeting.sort(key=lambda x: (x[1], x[0])) #두번째 인덱스
#print(meeting)  
# [[(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

et = 0  # end_time 회의 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= et:  # 회의 끝나는 시간 # 처음은 0이니까 무조건 참
        et = e
        cnt += 1
print(cnt)