import sys

if __name__ == "__main__":
    K = int(sys.stdin.readline())
    stack = []

    for _ in range(K):
        num = int(sys.stdin.readline())

        if num == 0 and len(stack) != 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))