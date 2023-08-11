num = int(input())
res=''

for _ in range(num):
    count, input_str = input().split()
    for i in range(len(input_str)):
        res+=input_str[i]*int(count)
    res+='\n'

print(res)