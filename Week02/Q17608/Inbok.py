import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    stack = []

    for _ in range(N):
        stack.append(int(sys.stdin.readline()))

    target = stack.pop()
    cnt = 1

    while len(stack) != 0:
        next = stack.pop()

        if next > target:
            target = next
            cnt += 1

    print(cnt)