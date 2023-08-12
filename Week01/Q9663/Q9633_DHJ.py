import sys

N = int(sys.stdin.readline())

answer = 0
row = [0] * N # N = 2 라면 [0, 0], N = 4 라면 [0, 0, 0, 0] 이 표시됨

def is_possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def queen(x):
    global answer #global
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i #(x, i)에 말을 놓을 수 있나?
            if is_possible(x): #가능하다면
                queen(x + 1)

queen(0)
print(answer)