from queue import PriorityQueue
import sys

if __name__ == "__main__":
    pQueue = PriorityQueue()
    N = int(sys.stdin.readline())

    for _ in range(N):
        num = int(sys.stdin.readline())

        if num == 0:
            if pQueue.qsize() == 0:
                print(0)
            else:
                print(pQueue.get()[1])
        else:
            pQueue.put(((-1 * num), num))