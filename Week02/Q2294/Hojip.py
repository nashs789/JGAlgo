import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
check = [0 for _ in range(100001)]

givenCoin = []
for i in range(n) :
    givenCoin.append(int(sys.stdin.readline()))

def BFS() :
    q = deque()
    
    for i in givenCoin : # 3개 다 q에 append
        cnt = 1 #하나씩 사용한것으로 처리, cnt 1
        q.append((i, cnt))
        check[i] = 1 # 코인 1개 사용체크
    
    while q :
        coin, cnt = q.popleft() # 코인,카운트 꺼내옴
        if coin == k : # 코인이 k와 같다면
            return cnt # cnt를 꺼내옴
        
        for j in givenCoin : # 코인세개를 돌아서
            sum = coin+j # 코인에 하나씩 더해봄
            if sum > k : # 만약 합친게 k보다 크다면 무시하고 다음것으로 넘어감.
                continue
            elif check[sum] == 0 : # sum을 check하는 자리가 비어있다면
                check[sum] = 1 # sum을 체크해줌.
                q.append((sum, cnt+1)) #sum과 cnt를 한개 더 한것을 q에 집어넣음.
    return -1

print(BFS())