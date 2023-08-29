import sys
input = sys.stdin.readline

n,k= map(int,input().split())
coin =[]
result=0

for _ in range(n):
    a=int(input())
    coin.append(a)
    
coin.sort(reverse=True)

for i in coin:
    if k==0:
        break
    result += k//i
    k %= i

print(result)