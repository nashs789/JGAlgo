sentence = input().strip()
word_list = list(sentence.split())
print(len(word_list))


#trim(): 파이썬에서는 strip()으로 사용됨
#strip(): string에서 앞, 뒤의 공백을 제거해주는 메소드
# lstrip(): 왼쪽의 공백만 제거
# rstrip(): 오른쪽의 공백만 제거
# replace(): 모든 공백 제거