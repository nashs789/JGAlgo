import sys
N, K = map(int, sys.stdin.readline().split())

level = list(int(sys.stdin.readline()) for i in range(N))
level.sort()

T = level[0]
gap = []
for i in range(0, N - 1):
    gap.append(level[i + 1] - level[i])


#K <= gap[0] % 1 + gap[1] % 2 + gap[2] % 3 + 4*gap[3] + ...

for i in range(len(gap)):
    if K >= gap[i] * (i + 1):
        T = T + gap[i]
        K = K - gap[i] * (i + 1)
    else:
        T = T + K // (i + 1)

if level[-1] == T:
    T = T + (K // N)
#이후로 모든 캐릭터의 레벨이 같아졌다면 남은 K 를 N 으로 나눈 몫만큼 레벨이 올라간다.

print(T)