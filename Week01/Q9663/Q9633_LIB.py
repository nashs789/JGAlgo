import sys
sys.setrecursionlimit(10**9)

N = int(input())
answer = 0
visited1 = [False] * N
visited2 = [False] * (N * 2 - 1)
visited3 = [False] * (N * 2 - 1)

def backTracking(row:int) -> None:
    global answer
    
    if row == N:
        answer += 1
        return
    
    for idx in range(N):
        if not visited1[idx] and not visited2[row + idx] and not visited3[row - idx + (N - 1)]:
            visited1[idx] = visited2[row + idx] = visited3[row - idx + (N - 1)] = True
            backTracking(row + 1)
            visited1[idx] = visited2[row + idx] = visited3[row - idx + (N - 1)] = False

backTracking(0)
print(answer)
