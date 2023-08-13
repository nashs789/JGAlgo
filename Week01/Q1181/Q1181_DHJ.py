import sys
N = int(sys.stdin.readline())
word_list= []
for i in range(N):
    word = sys.stdin.readline()
    word_list.append(word)                    #단어를 받아 리스트를 생성
word_set = set(word_list)                   
cleaned_list = list(word_set)                 #set로 중복 제거 리스트
word_list_list = []                           #단어 리스트를 받을 리스트 생성
for i in cleaned_list:
    chopped_word = list(i)                    #단어를 리스트화
    chopped_word.pop()                        
    word_list_list.append(chopped_word)       #단어 리스트 리스트를 생성

word_list_list.sort()                         #알파벳 순으로 정렬됨

final_list = sorted(word_list_list, key=len)  #sort 할 때 key = len을 입력하면 길이를 기준으로 정렬한다. 
                                              #데이터 타입에 상관없이 해당 데이터 타입의 길이만 봄.
for i in final_list:
    print(''.join(i))