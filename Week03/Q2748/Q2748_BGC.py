
# 피보나치 수는 0과 1로 시작
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1 -> 1
# 그럼 초반부인 0과 1인 경우는 예외 처리를 해주자

import sys
input = sys.stdin.readline

n = int(input())

# 피보나치 수를 저장하는 리스트
fibo =[]

# 초반 예외 처리
fibo.append(0)
fibo.append(1)

# 리스트에 피보나치 수를 계산하여 저장
for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n])
