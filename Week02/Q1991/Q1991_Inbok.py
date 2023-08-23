import sys

def order(node, order_tpye):
    if node != ".":
        if order_tpye == 0:
            print(node, end="")

        order(tree[node][0], order_tpye)

        if order_tpye == 1:
            print(node, end="")

        order(tree[node][1], order_tpye)
        
        if order_tpye == 2:
            print(node, end="")

if __name__== "__main__":
    input = sys.stdin.readline
    N = int(input())
    root_node = "A"
    tree = {}

    for _ in range(N):
        node, left, right = input().split()
        tree[node] = (left, right)

    order(root_node, 0)
    print()
    order(root_node, 1)
    print()
    order(root_node, 2)