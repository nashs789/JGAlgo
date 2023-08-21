import sys
from queue import PriorityQueue

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    pQueue = PriorityQueue()
    result = 0

    for _ in range(N):
        pQueue.put(int(sys.stdin.readline()))

    while pQueue.qsize() != 1:
        num1 = pQueue.get()
        num2 = pQueue.get()
        result += num1 + num2

        pQueue.put(num1 + num2)

    print(result)