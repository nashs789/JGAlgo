import sys
sys.setrecursionlimit(10 ** 5)

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def postorder(self):
        if self.left != None:
            self.left.postorder()

        if self.right != None:
            self.right.postorder()

        print(self.value)

if __name__ == "__main__":
    tree = Tree(int(sys.stdin.readline()))

    while True:
        try:
            tree.insert(int(sys.stdin.readline()))
        except:
            break

    tree.postorder()

# import sys
# sys.setrecursionlimit(10 ** 5)

# def postorder(left, right):
#     if left > right:
#         return
    
#     mid = right + 1

#     for node in range(left + 1, right + 1):
#         if graph[left] < graph[node]:
#             mid = node
#             break

#     postorder(left + 1, mid - 1)
#     postorder(mid, right)
#     print(graph[left])

# if __name__ == "__main__":
#     graph = []

#     while True:
#         try:
#             graph.append(int(sys.stdin.readline()))
#         except:
#             break

#     postorder(0, len(graph)-1)