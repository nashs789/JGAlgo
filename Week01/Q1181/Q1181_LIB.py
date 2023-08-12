import sys

count = int(sys.stdin.readline())
word_list = []

for _ in range(count):
    word_list.append(sys.stdin.readline().strip('\n'))

word_list = sorted(word_list, key=lambda x: (len(x), x))
word_set = set()

for word in word_list:
    if not word in word_set:
        word_set.add(word)
        print(word)