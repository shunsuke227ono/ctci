from LinkedList import *
class Stack(object):
    def __init__(self):
        self.pointer = -1
        self.array = []
    def push(self, node):
        self.array.append(node)
        self.pointer += 1
    def peek(self):
        return self.array[self.pointer]
    def pop(self):
        if self.isEmpty():
            return None
        node = self.array[self.pointer]
        self.array[self.pointer] = None
        self.pointer -= 1
        return node
    def size(self):
        return self.pointer + 1
    def isEmpty(self):
        return self.size() == 0

# Test

# stack = Stack()
# stack.push(Node(1))
# stack.push(Node(2))
# stack.push(Node(4))
# stack.push(Node(5))
#
# print stack.pop()
# print stack.peek()
# print stack.pop()
# print stack.pop()
# print stack.pop()
# print stack.pop()
# print stack.pop()
# print stack.pop()
# print stack.pop()
