import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())                                       # 추 개수
    chu_list = list(map(int, input().strip().split()))     # 추
    M = int(input())                                       # 구슬 개수
    ball_list = list(map(int, input().strip().split()))    # 구슬

    dp = [False for _ in range(40001)]
    dp[0] = True

    for chu in chu_list:
        Set = set()
        
        for weight in range(40001):
            if dp[weight]:
                if chu + weight <= 40000:
                    Set.add(chu + weight)
                Set.add(abs(chu - weight))

        for weight in Set:
            dp[weight] = True

    for ball in ball_list:
        print("Y" if dp[ball] else "N", end=" ")