import sys
from collections import deque

def is_empty():
    if len(queue) == 0:
        return True
    return False

if __name__ == "__main__":
    queue = deque([])
    N = int(sys.stdin.readline())

    for _ in range(N):
        reg = sys.stdin.readline().strip('\n').split()

        if reg[0] == "push":
            queue.append(reg[1])
        elif reg[0] == "pop":
            if is_empty():
                print(-1)
            else:
                print(queue.popleft())
        elif reg[0] == "size":
            print(len(queue))
        elif reg[0] == "empty":
            if is_empty():
                print(1)
            else:
                print(0)
        elif reg[0] == "front":
            if is_empty():
                print(-1)
            else:
                print(queue[0])
        elif reg[0] == "back":
            if is_empty():
                print(-1)
            else:
                print(queue[-1])