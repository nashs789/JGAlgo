A, B = map(int, input().split())
A_str = str(A)
B_str = str(B)
list_A = list(A_str)
list_B = list(B_str)

list_A.reverse()
list_B.reverse()

sangsu_A = int(''.join(list_A))
sangsu_B = int(''.join(list_B))

if sangsu_A - sangsu_B > 0:
    print(sangsu_A)
else:
    print(sangsu_B)