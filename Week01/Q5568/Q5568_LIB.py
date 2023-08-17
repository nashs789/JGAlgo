import sys

def backTracking(combIdx):
    if combIdx == k:
        Set.add("".join(combList))
        return
    
    for idx in range(0, n):
        if visited[idx]:
            continue

        visited[idx] = True
        combList[combIdx] = card[idx]
        backTracking(combIdx+1)
        visited[idx] = False

n = int(input())
k = int(input())
visited = [False for _ in range(n)]
combList = [0 for _ in range(k)]
card = []
Set = set()

for _ in range(n):
    card.append(input())

backTracking(0)
print(len(Set))