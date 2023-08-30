import sys
input=sys.stdin.readline

t=int(input())


for i in range(t):
    n=int(input())
    rank=[]
    for j in range(n):
        x,y = map(int,input().split())
        rank.append([x,y])
    rank.sort(key=lambda x: x[0])

    top = rank[0][1]
    num=1
    for i in range(1,n):
        if rank[i][1]<top:
            top=rank[i][1]
            num+=1

    print(num)