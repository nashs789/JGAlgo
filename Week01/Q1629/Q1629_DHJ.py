import sys
A, B, C = map(int, sys.stdin.readline().split())
# 지수 법칙 
  # A^m+n = A^m x A^n
# 나머지 분배 법칙
  # (AxB)%C = (A%C) * (B%C) % C

#즉, 10 ** 11 % 12 = 
# [{(10**5) % 12} * {(10**5) % 12} * 10**1] % 12 = 
# ((10**2)%12 * (10**2)%12 * 10)%12 * (10**2)%12 * (10**2)%12 * 10

def multiply(a,n):
    if n == 1:
        return a%C
    else:
        temp = multiply(a, n//2)
        if n%2 == 0:
            return (temp * temp) % C
        else:
            return(temp * temp * a) % C
print(multiply(A, B))