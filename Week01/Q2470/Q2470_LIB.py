import sys

N = int(sys.stdin.readline())
liq_list = list(map(int, sys.stdin.readline().split()))
liq_list.sort()
left, right = 0, len(liq_list) - 1
min_value = sys.maxsize
liq1, liq2 = liq_list[left], liq_list[right]

while left < right:
    mixed = abs(liq_list[left] + liq_list[right])

    if mixed == 0:
        print(liq_list[left], liq_list[right])
        sys.exit()

    if min_value > mixed:
        min_value = mixed
        liq1, liq2 = liq_list[left], liq_list[right]

    if liq_list[left] + liq_list[right] < 0:
        left += 1
    else:
        right -= 1

print(liq1, liq2)
