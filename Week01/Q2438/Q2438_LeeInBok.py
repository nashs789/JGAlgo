num = int(input()) + 1

for i in range(1, num):
    for j in range(0, i):
        print("*", end="")
    print()