import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        string = list(sys.stdin.readline().strip('\n'))
        stack = []

        for char in string:
            if char == "(":
                stack.append(char)
            else:
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    stack.append(char)

        if len(stack) == 0:
            print("YES")
        else:
            print("NO")