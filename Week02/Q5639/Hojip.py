import sys
sys.setrecursionlimit(10**6)

tmpList = []
while True:
    try :
        tmpList.append(int(sys.stdin.readline()))
    except :
        break


class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self, head): 
        self.head = head 
    
    #노드 삽입 메소드
    def insert_node(self, value):
        self.base_node = self.head 
        while True:
            if self.base_node.value > value: 
                if self.base_node.left != None: 
                    self.base_node = self.base_node.left 
                else: 
                    self.base_node.left = Node(value) 
                    break
            else: 
                if self.base_node.right != None: 
                    self.base_node = self.base_node.right 
                else: 
                    self.base_node.right = Node(value) 
                    break

head = Node(tmpList[0])

bt = BinarySearchTree(head)
for i in range(1, len(tmpList)) :
    bt.insert_node(tmpList[i])

def postorder(root) :
    if root == None :
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)

postorder(head)