
n=int(input())
chu_list = list(map(int,input().split()))
m=int(input())
marble_list =list(map(int,input().split()))

dp = [ 0 ] 
for chu in chu_list:
    tmp=[]
    for i in dp:
        tmp.append(i+chu)
        tmp.append(abs(i-chu))
    dp = list(set((dp + tmp)))

for chu in marble_list:
    if chu in dp:
        print('Y',end=' ')
    else:
        print('N',end=' ')