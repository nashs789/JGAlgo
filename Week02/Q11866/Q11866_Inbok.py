import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    queue = deque([])
    answer = []
    hit = 1

    for idx in range(1, N + 1):
        queue.append(idx)

    while len(queue) != 0:
        for _ in range (len(queue)):
            if hit == K:
                answer.append(queue.popleft())
                hit = 1
            else:
                queue.append(queue.popleft())
                hit += 1

    s = "<"

    for val in answer:
        s += str(val) + ", "

    s = s[:-2]
    s += ">"

    print(s)