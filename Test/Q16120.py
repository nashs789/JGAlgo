import sys

if __name__ == "__main__":
    string = list(sys.stdin.readline().strip("\n"))
    ppap = ["P", "P", "A", "P"]
    stack = []

    for ch in string:
        stack.append(ch)

        if stack[-4:] == ppap:
            for _ in range(3):
                stack.pop()

    if stack == ppap or "".join(stack) == "P":
        print("PPAP")
    else:
        print("NP")