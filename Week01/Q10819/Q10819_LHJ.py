import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

def backtrack(depth):
    global totalNum
    if depth == N:
        totalNum = sum(abs(combLst[i] - combLst[i + 1]) for i in range(N-1))
        result.add(totalNum)
        print('return')
        return
    for i in range(N):
        if visited[i]:
            continue
        combLst.append(A[i])
        visited[i] = True
        backtrack(depth + 1)
        visited[i] = False
        combLst.pop()

result = set()
combLst = []
visited = [False] * N

backtrack(0)

print(max(result))