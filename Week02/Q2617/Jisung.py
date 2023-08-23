import sys

bead_N, edge = map(int, sys.stdin.readline().strip().split())

heavy_bead_list = [[] for _ in range(bead_N + 1)]
light_bead_list = [[] for _ in range(bead_N + 1)]
for _ in range(edge):
    heavy, light = map(int, sys.stdin.readline().strip().split())
    heavy_bead_list[light].append(heavy)
    light_bead_list[heavy].append(light)

def dfs(node, list):
    global visited
    global check
    visited[node] = 1
    for bead in list[node]:
        if visited[bead] == 0:
            check += 1
            dfs(bead, list)



count = 0
md = (bead_N + 1) / 2
for i in range(1, bead_N + 1):
    visited = [0] * (bead_N + 1)

    check = 0
    dfs(i, heavy_bead_list)
    if (check >= md):
        count += 1

    check = 0
    dfs(i, light_bead_list)
    if check >= md:
        count += 1


print(count)