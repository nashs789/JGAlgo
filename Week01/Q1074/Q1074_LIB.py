# import sys
# sys.setrecursionlimit(10**9)

# N, r, c = map(int, sys.stdin.readline().split())
# N = pow(2, N);
# cnt = -1

# def search(x, y, n):
#     global r, c, cnt

#     print(x, y, n, n//2)

#     if n != 2:
#         calc = n//2
#         calc_double = calc * calc

#         if r < calc and c < calc:
#             print("1사분면")
#             search(x, y, calc)
#         elif r < calc and calc <= c:
#             print("2사분면")
#             cnt += calc_double
#             search(x, y + n // 2, calc)
#         elif calc <= r and c < calc:
#             print("3사분면")
#             cnt += calc_double * 2
#             search(x + calc, y, calc)
#         else:
#             print("4사분면")
#             cnt += calc_double * 3
#             search(x + calc, y + calc, calc)
#         return

#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             cnt += 1
#             if r == i and c == j:
#                 print(cnt)
#                 sys.exit()
                
# search(0, 0, N)

import sys
sys.setrecursionlimit(10**9)

N, r, c = map(int, sys.stdin.readline().split())
N = pow(2, N);
cnt = -1

def search(x, y, n):
    global r, c, cnt

    if n != 2:
        calc = n//2
        calc_double = calc * calc

        if x <= r < x + calc and y <= c < y + calc:
            search(x, y, calc)
        elif x <= r < x + calc and y + calc <= c < y +calc + calc:
            cnt += calc_double
            search(x, y + n // 2, calc)
        elif x + calc <= r < x +calc + calc and y <= c < y + calc:
            cnt += calc_double * 2
            search(x + calc, y, calc)
        else:
            cnt += calc_double * 3
            search(x + calc, y + calc, calc)
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            cnt += 1
            if r == i and c == j:
                print(cnt)
                sys.exit()
                
search(0, 0, N)