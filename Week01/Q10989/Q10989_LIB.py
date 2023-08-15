import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num_count = [0] * 10001

    for _ in range(N):
        num_count[int(sys.stdin.readline())] += 1

    for idx, val in enumerate(num_count):
        while val != 0:
            print(idx)
            val -= 1
