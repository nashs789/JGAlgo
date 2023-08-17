import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
min_value = sys.maxsize
max_value = -sys.maxsize - 1

def backTracking(listIdx, total):
    global max_value
    global min_value

    if listIdx == N:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return
    
    for idx in range(4):
        if operators[idx] != 0:
            operators[idx] -= 1
            
            if idx == 0:
                backTracking(listIdx + 1, total + num_list[listIdx])
            elif idx == 1:
                backTracking(listIdx + 1, total - num_list[listIdx])
            elif idx == 2:
                backTracking(listIdx + 1, total * num_list[listIdx])
            else:
                backTracking(listIdx + 1, div(total, num_list[listIdx]))

            operators[idx] += 1
             
def div(num1, num2):
    if num1 < 0:
        num1 *= -1
        return -1 * (num1 // num2)

    return num1 // num2

backTracking(1, num_list[0])
print(max_value)
print(min_value)