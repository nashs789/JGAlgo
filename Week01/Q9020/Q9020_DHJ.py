def is_prime(n):
      if n <= 1:
        return False
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
      return True

def goldbach_partition(n):
  prime_list = [i for i in range(2, n) if is_prime(n)]
  list_a = []
  list_b = []
  for i in prime_list:
    if (n - i) in prime_list:
      list_a.append(i)
      list_b.append(n - i)
        
  if len(list_a) >= 2:
      min_diff = abs(list_b[0] - list_a[0])
      min_diff_index = 0
      for i in range(1, len(list_a)):
         diff = abs(list_b[i] - list_a[i])
         if diff <min.diff:
            min_diff = diff
            min_diff_index = i
      return list_a[min_diff_index], list_b[min_diff_index]

T = int(input())
for i in range(T):
    n = int(input())
    partition = goldbach_partition(n)
    if partition is not None:
       print(partition[0], end=" ")
       print(partition[1])