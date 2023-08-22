import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    front_heap = []
    back_heap = []
    cnt = 0
    N = int(sys.stdin.readline())

    for _ in range(N):
        num = int(sys.stdin.readline())

        if cnt % 2 == 0:
            heappush(front_heap, (-num, num))
        else:
            heappush(back_heap, (num, num))
        print(left,right)

        if len(back_heap) != 0 and front_heap[0][1] > back_heap[0][1]:
            temp = heappop(front_heap)[1]
            back_num = heappop(back_heap)[1]
            heappush(front_heap, (-back_num, back_num))
            heappush(back_heap, (temp, temp))
        
        cnt += 1
        print(front_heap[0][1])