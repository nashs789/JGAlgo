import sys

treeCnt, meter = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(trees)

def func():
    global left, right
    while left <= right:
        mid = (left + right) // 2
        sum = 0
        
        for item in list(filter(lambda x: x > mid, trees)):
            sum += item - mid

        if sum >= meter:
            left = mid + 1
        else:
            right = mid - 1

func()
print(left - 1)