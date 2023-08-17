import sys

def backTracking(peopleIdx, combIdx):
    if combIdx == 7:
        if sum(comb) == 100:
            for item in sorted(comb):
                print(item)
            sys.exit()
        return
    
    for idx in range(peopleIdx, 9):
        if not visited[idx]:
            visited[idx] = True
            comb[combIdx] = people[idx]
            backTracking(peopleIdx + 1, combIdx + 1)
            visited[idx] = False


people = []
comb = [0] * 7
visited = [False] * 9

for _ in range(9):
    people.append(int(input()))

backTracking(0, 0)