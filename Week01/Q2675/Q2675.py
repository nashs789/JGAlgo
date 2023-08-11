T = int(input())

for _ in range(T):
    repeat, val = input().split()
    
    for item in val:
        print(item * int(repeat), end="")
    print()