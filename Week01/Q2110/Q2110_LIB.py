import sys

N, C = map(int, sys.stdin.readline().split())
router_list = [] 

for _ in range(N):
    router_list.append(int(sys.stdin.readline()))

router_list.sort()
left, right = 0, router_list[-1] - router_list[0]
answer = 0

def binary_search():
    global left, right, answer
    
    while left <= right:
        mid = (left + right) // 2
        router_cnt = C - 1
        cur_router = router_list[0]

        for idx in range(1, N):
            dist = router_list[idx] - cur_router

            if dist >= mid:
                router_cnt -= 1
                cur_router = router_list[idx]

            if router_cnt == 0:
                break
        # 코드 쫌 구진데 개선해야하는데....
        if router_cnt == 0:
            answer = mid

        if router_cnt > 0:
            right = mid - 1
        else:
            left = mid + 1
        
binary_search()
print(answer)