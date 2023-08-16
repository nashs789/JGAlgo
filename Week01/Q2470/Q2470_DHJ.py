import sys
N = int(sys.stdin.readline())
ph = list(map(int, sys.stdin.readline().split()))
ph.sort()

start = ph[0]
end = ph[-1]
mid = start + end
mixture = abs(0 - mid)
prev_mixture = mixture
result_start = 0
result_end = 0

for i in range(1, N):
    if prev_mixture < mixture:
        print(prev_start, end=' ')
        print(prev_end)
        print('result_start')
        result_start = prev_start
        print(result_start)
        print('result_end')
        result_end = prev_end
        print(result_end)
        break
    else:    
        if mid < 0:
            prev_start = start
            prev_end = end
            start = ph[i]
            mid = start + end
            prev_mixture = mixture
            print('mixture_in_loop_sub_zero')
            mixture = abs(0 - mid)
            print(mixture)
        elif mid == 0:
            result_start = start
            result_end = end
            break
        else:
            prev_start = start
            prev_end = end
            end = ph[(i*-1) - 1]
            mid = start + end
            prev_mixture = mixture
            print('mixture_in_loop_over_zero')
            mixture = abs(0 - mid)
            print(mixture)
        result_start = start
        result_end = end

print('final_answer')        
print(result_start, end=' ')
print(result_end)       
    