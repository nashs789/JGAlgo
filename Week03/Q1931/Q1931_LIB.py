import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    schedule = []

    for _ in range(N):
        srt, end = map(int, input().strip().split())
        schedule.append((srt, end))

    schedule.sort(key = lambda x: (x[1], x[0]))

    cnt = 1
    end_time = schedule[0][1]

    for next_schedule in range(1, N):
        if schedule[next_schedule][0] >= end_time:
            cnt += 1
            end_time = schedule[next_schedule][1]

    print(cnt)