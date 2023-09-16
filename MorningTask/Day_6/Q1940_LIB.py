import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num_list = list(map(int, input().strip().split()))
ans = 0
num_list.sort()

left, right = 0, N - 1

while left < right:
    num_sum = num_list[left] + num_list[right]

    if num_sum == M:
        ans += 1

    if num_sum > M:
        right -= 1
    else:
        left += 1

print(ans)