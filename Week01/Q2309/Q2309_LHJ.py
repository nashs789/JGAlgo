import sys
dwarfs = [] * 9
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

diff = sum(dwarfs) - 100
flag = False
for k in range(0, 8):
    if flag : break
    for i in range(k+1, 9):
        if dwarfs[k] + dwarfs[i] == diff:

            eight, nine = dwarfs[k], dwarfs[i]
            dwarfs.remove(eight)
            dwarfs.remove(nine)
            flag = True
            break
dwarfs.sort()
for dwarf in dwarfs: print(dwarf)
    

# sort_dwarf(7)

# def sort_dwarf(count):
#     if count == 1:
#         return
#     for i in range(1, count):
#         if dwarfs[i-1] > dwarfs[i]:
#             dwarfs[i-1], dwarfs[i] = dwarfs[i], dwarfs[i-1]
#         sort_dwarf(count-1)
