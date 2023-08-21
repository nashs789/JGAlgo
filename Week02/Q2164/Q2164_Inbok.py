import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    flag = 0
    queue = deque([])

    for idx in range(1, N + 1):
        queue.append(idx)

    while len(queue) != 1:
        if flag % 2 == 0:
            flag += 1
            queue.popleft()
        else:
            flag -= 1
            queue.append(queue.popleft())

print(queue.popleft())