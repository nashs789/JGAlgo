import sys
input = sys.stdin.readline

exp = input().strip().split('-') 
ans = 0

for i in exp[0].split('+'):
    ans += int(i)

for i in exp[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)