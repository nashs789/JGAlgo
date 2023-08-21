import sys

class Stack:
    __arr = []

    def push(self, n:int):
        self.__arr.append(n)

    def pop(self):
        if self.is_empty():
            return -1
        
        return self.__arr.pop()
    
    def size(self):
        return len(self.__arr)
    
    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0
    
    def top(self):
        if self.is_empty():
            return -1
        
        return self.__arr[-1]
    
    def is_empty(self):
        if len(self.__arr) == 0:
            return True
        return False

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    stack = Stack()

    for _ in range(N):
        reg = sys.stdin.readline().split()

        if reg[0] == "push":
            stack.push(reg[1])
        elif reg[0] == "pop":
            print(stack.pop())
        elif reg[0] == "size":
            print(stack.size())
        elif reg[0] == "empty":
            print(stack.empty())
        elif reg[0] == "top":
            print(stack.top())