import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    liquids = list(map(int, input().strip().split()))
    best_value = sys.maxsize
    best_pair = None;

    left, right = 0, N - 1

    while left < right:
        result = liquids[left] + liquids[right]

        if best_value > abs(result):
            best_value = abs(result)
            best_pair = (liquids[left], liquids[right])
        
        if result == 0:
            break
        elif result <= 0:
            left += 1
        else:
            right -= 1

    print(best_pair[0], best_pair[1])