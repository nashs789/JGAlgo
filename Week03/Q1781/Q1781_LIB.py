import sys
from heapq import heappop, heappush
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    info = []
    pQueue = []
    
    for _ in range(N):
        deadline, noodle = map(int, input().strip().split())
        info.append((deadline, noodle))

    info.sort(key=lambda x: x[0])

    for deadline, noodle in info:
        heappush(pQueue, noodle)

        if deadline < len(pQueue):
            heappop(pQueue)

    print(sum(pQueue))