import sys
from typing import Any,Type

class Node:
	def ___init__(self, key:Any, value:Any, left: Node=None, right: Node=None):
		self.key = key
		self.value = value
		self.left = left
		self.right = right
		
class BinarySearchTree:
	
    def __init__(self):
        self.root = None
    
    def search(self, key:Any):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
            

input = sys.stdin.readline

root = int(input())
tree = {}

while True:
	try:
		tree.append(int(input()))
	except:
		break



binary_tree(0, len(tree)-1)