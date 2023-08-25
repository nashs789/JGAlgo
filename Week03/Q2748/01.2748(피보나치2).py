# import sys

# n = int(sys.stdin.readline())


# def fibo(n):
    
#     if n==1 or n==2:
#         return 1
#     else:
#         return (fibo(n-1)+fibo(n-2))
    
# ans=fibo(n)

# print(ans)

#동적 피보나치

import sys
n = int(sys.stdin.readline())
def fibo2(n):
    f = [0] * (n + 1)  # 리스트 초기화
    
    f[0] = 0
    f[1] = 1
    
    for i in range(2, n + 1):
        f[i] = f[i - 2] + f[i - 1]
    
    return f[n]

ans = fibo2(n)
print(ans) 



# import sys

# n = int(sys.stdin.readline())

# def fibo2(n):
#     f = [0] * (n+2)  # 리스트 초기화

#     f[1] = 1
#     f[2] = 1
    
#     for i in range(3, n+1):
#         f[i] = f[i - 1] + f[i - 2]
#     return f[n]

# ans = fibo2(n)
# print(ans) 