x, y, w, h = map(int, input().split())

value = (x, abs(w-x), y, abs(h-y))
print(min(value))