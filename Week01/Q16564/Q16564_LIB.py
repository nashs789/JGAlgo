import sys

N, K = map(int, sys.stdin.readline().split())
hero = []

for _ in range(N):
    hero.append(int(sys.stdin.readline()))

hero.sort()
left, right = hero[0], hero[-1] + K
max_level = 0

while left <= right:
    mid = (left + right) // 2
    level = K
    fail = False

    for idx in range(N):
        if hero[idx] > mid:
            continue

        level -= (mid - hero[idx])

        if level < 0:
            fail = True
            break;

    if fail:
        right = mid - 1
    else:
        left = mid + 1
        max_level = max(max_level, mid)

print(max_level)
