# 시간 초과
# import sys

# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     stack = list(map(int,sys.stdin.readline().split()))
#     dist_list = []

#     while len(stack) != 0:
#         top = stack.pop()
#         hit = False

#         for idx, high in reversed(list(enumerate(stack))):
#             if top <= high:
#                 dist_list.append(idx + 1)
#                 hit = True
#                 break

#         if not hit:
#             dist_list.append(0)
            
#     for idx in reversed(dist_list):
#         print(idx, end=" ")

# 스택을 전부 받지 않고 하나씩 입력 받으면서 인덱스 계산해서 할것
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    top_list = list(map(int,sys.stdin.readline().split()))
    stack = []

    for idx, top in enumerate(top_list):
        while len(stack) != 0 and stack[-1][1] < top:
            stack.pop()
        
        if len(stack) == 0:
            print(0, end=" ")
        else:
            print(stack[-1][0] + 1, end=" ")    # index는 0 부터 시작해서 +1 처리
                    
        stack.append((idx, top))