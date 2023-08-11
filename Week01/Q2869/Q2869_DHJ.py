import math
A, B, V = map(int,input().split())
print(math.ceil((V - B) / (A - B)))

#파이썬에서 올림, 버림, 반올림
#JS와 똑같지만 상단에서 import math가 필요한 점은 다르다. M이 대문자일 필요도 없음.