import sys

def is_prime(n):
      if n <= 1:
        return False
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
      return True

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    answer_list = []
    middle = n // 2
    k = 0
    while middle > 0:
        if is_prime(middle):
            if is_prime(n - middle):
                print(middle, n - middle)
                break
        middle -= 1