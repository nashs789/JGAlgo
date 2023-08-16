import sys
N = int(sys.stdin.readline())
ph = list(map(int, sys.stdin.readline().split()))
ph.sort()

start = 0 #시작과 끝을 배열 내 요소가 아닌 인덱스로 설정
end = N - 1

answer = abs(ph[start] + ph[end])
final = [ph[start], ph[end]]

while start < end:
    start_val = ph[start]
    end_val = ph[end]

    sum = start_val + end_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [start_val, end_val]
        if answer == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1
print(final[0], final[1])


# start = ph[0]
# end = ph[-1]
# mid = start + end
# mixture = abs(mid)
# minimum_mixture = mixture
# minimum_start = start
# minimum_end = end
# flip_flop = 0
# # print('first_mixture')
# # print(mixture)
# # print('first_minimum_mixture')
# # print(minimum_mixture)
# for i in range(N):
#     if len(ph) <= 2:
#         break

#     # print('minimum_now')
#     # print(minimum_start)
#     # print('-')
#     # print(minimum_end)
#     # print('-')
#     # print(minimum_mixture)
#     if mid == 0:
#         minimum_start = start
#         minimum_end = end
#         break
        
#     if flip_flop == 0:
#         ph.pop(0)
#         #print('start_in_flip_flop_0')
#         start = ph[0]
#         # print(start)
#         # print('end_in_flip_flop_0')
#         # print(end)
#         mid = start + end
#         #print('mixture_in_loop_flip_flop_0')
#         mixture = abs(mid)
#         #print(mixture)
#         flip_flop = 1
#     else:
#         ph.pop()
#         # print('start_in_flip_flop_1')
#         # print(start)
#         # print('end_in_flip_flop_1')
#         end = ph[-1]
#         #print(end)
#         mid = start + end
#         #print('mixture_in_loop_flip_flop_1')
#         mixture = abs(mid)
#         #print(mixture)
#         flip_flop = 0

#     if  minimum_mixture > mixture:
#         minimum_start = start
#         minimum_end = end
#         minimum_mixture = mixture
    

# #print('final_answer')        
# print(minimum_start, end=' ')
# print(minimum_end)       
    

# for i in range(1, N):
#     if minimum_mixture < mixture:
#         print(prev_start, end=' ')
#         print(prev_end)
#         print('result_start')
#         result_start = prev_start
#         print(result_start)
#         print('result_end')
#         result_end = prev_end
#         print(result_end)
#         break
#     else:    
#         if mid < 0:
#             prev_start = start
#             prev_end = end
#             start = ph[i]
#             mid = start + end
#             prev_mixture = mixture
#             print('mixture_in_loop_sub_zero')
#             mixture = abs(0 - mid)
#             print(mixture)
#         elif mid == 0:
#             result_start = start
#             result_end = end
#             break
#         else:
#             prev_start = start
#             prev_end = end
#             end = ph[(i*-1) - 1]
#             mid = start + end
#             prev_mixture = mixture
#             print('mixture_in_loop_over_zero')
#             mixture = abs(0 - mid)
#             print(mixture)
#         result_start = start
#         result_end = end