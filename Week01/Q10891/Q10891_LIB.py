import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
max_value = 0
new_seq = [0] * N
visited = [False] * N

def backTracking(seqIdx):
    global max_value
    global visited

    if seqIdx == N:
        max_value = max(max_value, get_new_seq_sum())
        return
    
    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            new_seq[seqIdx] = A[idx]
            backTracking(seqIdx + 1)
            visited[idx] = False

def get_new_seq_sum():
    new_sum = 0

    for idx in range(1, N):
        new_sum += abs(new_seq[idx - 1] - new_seq[idx])

    return new_sum

backTracking(0)
print(max_value)