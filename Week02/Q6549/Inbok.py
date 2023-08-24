import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    rec_list = []

    for _ in range(N):
        rec_list.append(int(input()))

    rec_list.append(0)
    stack = [(0, rec_list[0])]
    result = 0
    left = None
    
    for right in range(1, N + 1):
        left = right

        while stack and stack[-1][1] > rec_list[right]:
            left, height = stack.pop()
            result = max(result, height * (right - left))

        stack.append((left, rec_list[right]))

    print(result)