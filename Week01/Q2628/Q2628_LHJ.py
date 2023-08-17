import sys
w, h = map(int, (sys.stdin.readline().split()))
count = int(sys.stdin.readline())

width = [0, h]
height = [0, w]
for _ in range(count):
    bound, num = map(int, (sys.stdin.readline().split()))
    if bound == 0:
        width.append(num)
    else:
        height.append(num)

width.sort()
height.sort()

w_gap = [(width[i]-width[i-1]) for i in range(1, len(width))]
h_gap = [(height[i]-height[i-1]) for i in range(1, len(height))]

print(max(w_gap) * max(h_gap))