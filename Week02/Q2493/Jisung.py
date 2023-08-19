import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
stack = deque([])
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > list[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, list[i]])

print(" ".join(map(str, answer)))