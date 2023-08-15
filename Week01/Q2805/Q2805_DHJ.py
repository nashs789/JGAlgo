import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

def timber(f, r):
    while True:
        chain_saw = (f + r) // 2

        truck = []
        for tree in trees:
            if tree > chain_saw:
                truck.append(tree - chain_saw)
            else:
                truck.append(0)

        if sum(truck) == M or f > r:
            return chain_saw
        elif sum(truck) > M:
            f = chain_saw + 1
        else:
            r = chain_saw - 1

print(timber(0, trees[-1]))