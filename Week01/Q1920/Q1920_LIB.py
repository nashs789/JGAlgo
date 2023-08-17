import sys

N = int(sys.stdin.readline())
num_list = list(map(int, (sys.stdin.readline().split())))
M = int(sys.stdin.readline())
target = list(map(int, (sys.stdin.readline().split())))

num_list.sort()
left, right = 0, len(num_list) - 1

def binarySearch(left, right, num):
    while left <= right:
        mid = (left + right) // 2

        if num_list[mid] == num:
            print(1)
            return
        elif num_list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    print(0)

for num in target:
    binarySearch(left, right, num)