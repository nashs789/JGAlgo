import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
possible_list = [0] * N
visited = [0] * N
max_list = []


def perm(n, k):
    if n == k:
        total = 0
        for i in range(0,n - 1):
            absolute = abs(possible_list[i] - possible_list[i+1])
            total = total + absolute
        max_list.append(total)
            
        
    else:
        for i in range(0, n):
            if visited[i] : continue
            possible_list[k] = num_list[i]
            visited[i] = True
            perm(n, k+1)
            visited[i] = False


perm(N, 0)

print(max(max_list))
# import sys
# N = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# possible_list = [0] * N
# visited = [0] * N
# possible_list_list = []

# def permutation (n, k):
#     if n == k:
#         possible_list_list.append(possible_list)
#     else:
#         for i in range(0, n):
#             if visited[i]: 
#                 continue
#             possible_list[k] = num_list[i]
#             visited[i] = True
#             permutation(n, k + 1)
#             visited[i] = False

# permutation(N, 0)


# print(N)
# print(num_list)

# print(possible_list_list)
# total = 0
# max_list = []
# for i in possible_list_list:
#     for j in range(0, N - 1):
#       absolute = abs(i[j] - i[j + 1])
#       total = total + absolute
#     max_list.append(total)
    
# print(max_list)
# print(max(max_list))
# nPn 으로 정렬 가능한 순열을 계산하여 리스트로 출력
# abs(A[n] - A[n + 1])을 계산하고 이를 total 에 계속 더하는 함수

#while n > N:
#    absolute = abs(list[n] - list[n + 1])
#    total = total + absolute
#    n += 1
#max_list.append(total))
#print(max(max_list))
