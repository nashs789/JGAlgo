import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word1, word2 = input().strip(), input().strip()
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    cache = [0] * len(word2)

    for i in range(len(word1)):
        cnt = 0

        for j in range(len(word2)):
            if cnt < cache[j]:
                cnt = cache[j]
            elif word1[i] == word2[j]:
                cache[j] = cnt + 1

    print(max(cache))