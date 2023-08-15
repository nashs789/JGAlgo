import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
maybe_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
pl = 0 #첫 인덱스
pr = len(num_list) - 1 #마지막 인덱스

def search(list, target):
    pl = 0 #첫 인덱스
    pr = len(num_list) - 1 #마지막 인덱스

    while True:
      pc = (pl + pr) // 2 #가운데 인덱스
      if list[pc] == target:
          print(1)
          return
      elif list[pc] < target:
          pl = pc + 1 #첫 인덱스를 가운데 + 1로 변경
      else:
          pr = pc - 1 #마지막 인덱스를 가운데 - 1로 변경
      if pl > pr:
        print(0)
        break

for maybe in maybe_list:
    search(num_list, maybe)
      
        