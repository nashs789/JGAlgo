arr = input()
n= len(arr)

table =[[False]*(n) for i in range(n)]

for i in range(n):
    table[i][i]=True

#시작점과 끝점이 같을때 2글자일때
for i in range(n-1):
    if arr[i] == arr[i+1]:
        table[i][i+1]=True

for t in range(n-2):
    for i in range(n-2-t):
        j= i+t+2
        if arr[i] == arr[j] and table[i+1][j-1]:
            table[i][j]=True

dp=[0 for _ in range(n)]
dp[0] = 1
for i in range(1,n):
    min1 = dp[i-1]+1
    for j in range(i):
        if table[j][i]:
            min1=min(min1,dp[j-1]+1)
    dp[i]= min1
print(dp[-1])