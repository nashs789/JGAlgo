import sys

n = int(sys.stdin.readline())
dict = []

for i in range(n):
    dict.append(sys.stdin.readline().strip())

# 중복 삭제
sort_dict = set(dict)

dict = sorted(list(sort_dict))
dict.sort(key = len)

for i in dict:
    print(i)