import sys
M, N, L = map(int, sys.stdin.readline().split())

print(M)
print(N)
print(L)
gun = list(map(int, sys.stdin.readline().split()))
gun.sort()
print(gun)
animal = []
for i in range(N):
    animal.append(list(map(int, sys.stdin.readline().split())))
print(animal)

