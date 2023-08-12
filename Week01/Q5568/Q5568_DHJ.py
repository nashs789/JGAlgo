def permutation(index, temp_permutation):
    if index == k:
        answer_set.add(''.join(temp_permutation))
        return
    
    for i in range(len(card_list)):
        if visited[i]:
            continue
        else:
            temp_permutation.append(str(card_list[i]))
            visited[i] = True
            permutation(index + 1, temp_permutation)
            visited[i] = False
            temp_permutation.pop()


n = int(input())
k = int(input())
card_list = []
for i in range(0,n):
    card = int(input())
    card_list.append(card)

visited = []
for i in range(len(card_list)):
    visited.append(False)

answer_set = set()

permutation(0,[])

print(len(answer_set))



#for i in perm:
#    joined =int(''.join(map(str,i)))
#    answer_set.add(joined)
#print(len(answer_set))


#from itertools import permutations

#n = int(input())
#k = int(input())
#card_list = []
#for i in range(0,n):
#    card = int(input())
#    card_list.append(card)

#perm = list(permutations(card_list,k))

#answer_set = set()
#for i in perm:
#    joined =int(''.join(map(str,i)))
#    answer_set.add(joined)
#print(len(answer_set))

#순열, 조합
#파이썬에서 from itertools import permutation (순열) ,combination (조합) 으로 간단하게 할 수 있음

#튜플
#위에서 설명한 메소드를 사용하면 결과값이 튜플로 나온다.
#튜플은 리스트와 비슷하지만 a = (3,) 처럼 1개의 요소를 가지고 있을 떄에도 반드시 쉼표가 있어야 한다는 점과
#a = 1,2,3 처럼 소괄호를 생략해도 된다는 점이 다르다.

#튜플의 특징은 요소값을 변화할 수 없다는 점이 특징이다.
#그리고 ''.join()메소드를 사용하면 튜플 내의 데이터 타입이 string일 때는 합칠 수 있지만 integer일때는 불가능해서
#순열로 늘어놓은 카드를 합쳐서 하나의 정수를 만들 때 튜플 내의 값의 데이터 타입을 str로 변경했다가 다시 int 로 바꿔야 할 필요가 있었다.

#마지막으로.. 계산 다 해놓고 예제 입력해서 답도 맞게 나오는데 왜 틀렸다고 뜨는지 궁금해서 chatGPT 한테 물어본 결과
#joined로 받는 순열 값을 합친 것의 데이터 타입을 int로 변환하지 않아서 틀렸다고 뜨는 것이었다.