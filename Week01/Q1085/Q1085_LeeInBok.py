x, y, w, h = map(int, input().split())

arr = [x, y, w-x, h-y]
print(min(arr))