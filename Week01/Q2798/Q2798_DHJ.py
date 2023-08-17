def combinations(arr, n):
    result = []
    def backtrack(start, curr_combination):
        if len(curr_combination) == n:
            result.append(curr_combination[:])
            return
        for i in range(start, len(arr)):
            curr_combination.append(arr[i])
            backtrack(i + 1, curr_combination)
            curr_combination.pop()
    
    backtrack(0, [])
    return result

import sys
N, M = map(int,sys.stdin.readline().split())

card_list = list(input().split())
int_card_list = list(map(int, card_list))

maybe_list = combinations(int_card_list, 3)

diff_list = []

for maybe in maybe_list:
    sum_list = sum(maybe)
    if sum_list <= M:                 
        diff_list.append(M - sum_list)

absolute = sorted(diff_list, key=abs)

minimum_value = absolute[0]

print(M - minimum_value)




#card_list 에서 조합 N C 3으로 가능한 조합을 담은 maybe_list 생성
#for maybe in maybe_list:
#  list.append(M - sum(maybe)) 
# # 각 조합의 합과 M 과의 차이를 담은 list 생성
#이 때 가능한 리스트 내 요소들의 합을 더했을 때(즉, sum(maybe)가) M보다 크면 안 됨!
#min(list) 로 최소값 계산
# M - min(list) 를 출력