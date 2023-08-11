from itertools import permutations

n = int(input())
k = int(input())
card_list = []
for i in range(0,n):
    card = int(input())
    card_list.append(card)

perm = list(permutations(card_list,k))

answer_set = set()
for i in perm:
    joined =int(''.join(map(str,i)))
    answer_set.add(joined)
print(len(answer_set))

#순열, 조합
#파이썬에서 from itertools import permutation (순열) ,combination (조합) 으로 간단하게 할 수 있음

#튜플
#위에서 설명한 메소드를 사용하면 결과값이 튜플로 나온다.
#
#마지막으로.. 계산 다 해놓고 예제 입력해서 답도 맞게 나오는데 왜 틀렸다고 뜨는지 궁금해서 chatGPT 한테 물어본 결과
#joined로 받는 순열 값을 합친 것의 데이터 타입을 int로 변환하지 않아서 틀렸다고 뜨는 것이었다.