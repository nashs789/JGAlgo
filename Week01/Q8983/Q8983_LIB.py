import sys

M, N, L = map(int, sys.stdin.readline().split())
hunters = list(map(int, sys.stdin.readline().split()))
hunters.sort()
animals = []
count = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    animals.append((x, y))

def binarySearch(x, y):
    global left, right

    while left <= right:
        mid = (left + right) // 2   # 사격 하는 포대 인덱스

        if abs(hunters[mid] - x) + y <= L:
            return True

        if hunters[mid] - x < 0:
            left = mid + 1
        else:
            right = mid - 1

for idx, animal in enumerate(animals):
    left, right = 0, len(hunters) - 1

    if binarySearch(animal[0], animal[1]):
        count += 1

print(count)
