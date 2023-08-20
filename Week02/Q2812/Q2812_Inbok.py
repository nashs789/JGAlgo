import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    num_list = list(sys.stdin.readline().strip('\n'))
    stack = []

    for idx, val in enumerate(num_list):
        digit = num_list[idx]

        while K > 0 and len(stack) != 0 and stack[-1] < digit:
            K -= 1
            stack.pop()

        stack.append(digit)

    while K != 0:
        K -= 1
        stack.pop()

    print("".join(stack))