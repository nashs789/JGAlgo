import sys

N = int(sys.stdin.readline())

answer = 0
position = [0] * N
row = [False] * N
idx_7 = [False] * (2 * N - 1)
idx_4 = [False] * (2 * N - 1)

def is_possible(i):
    for j in range(i):
        if row[j] or idx_7[j+i] or idx_4[j-i+N-1]:
            return False
    return True

def queen(i):
    global answer

    if i == N:
        answer += 1
        return
    else:
        for j in range(N):
            position[i] = j
            if is_possible(i):
                row[j] = True
                idx_7[j+i] = True
                idx_4[j-i+N-1] = True
                queen(i+1)
                row[j] = False
                idx_7[j+i] = False
                idx_4[j-i+N-1] = False

queen(0)
print(answer)

#global 로 전역변수를 사용할 때 함수 밖에서 선언한다면 함수 안에서 사용할 때 또 global로 전역 변수를 선언해야 함.