import sys
N = int(sys.stdin.readline())
n_nums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_nums = list(map(int, sys.stdin.readline().split()))

def binarySearch(m, start, end):
    while start <= end:
        mid=(start+end)//2
        if m > nLst[mid]: start = mid+1
        elif m < nLst[mid]: end = mid-1
        elif m == nLst[mid]:
            print(1)
            return
    print(0)

nLst = sorted(n_nums)
for m in m_nums: binarySearch(m, 0, N-1)