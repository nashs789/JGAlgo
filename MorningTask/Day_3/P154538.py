from collections import deque
# stack
def solution(x, y, n):
    is_out = 0
    stack = deque([0,0])
    cnt = 0
    while is_out < 1000000:
        while stack:
            temp = stack.popleft()
            print(temp[0])
            if temp[0]==y:
                return temp[1]
        cnt += 1
        is_out = cnt * x * 2
        stack.append([x*n,cnt])
        stack.append([2*x,cnt])
        stack.append([3*x,cnt])
    return -1