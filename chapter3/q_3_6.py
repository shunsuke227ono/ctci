class SortStack(object):
    def __init__(self, stack):
        self.stack = stack
    def sort(self):
        sorted_stack = []
        while len(self.stack) != 0:
            self.move_one(sorted_stack)
        self.stack = sorted_stack
    def move_one(self, sorted_stack):
        current = self.stack.pop()
        while len(sorted_stack) != 0 and sorted_stack[-1] < current:
            self.stack.append(sorted_stack.pop())
        sorted_stack.append(current)
        while len(self.stack) != 0 and self.stack[-1] < sorted_stack[-1]:
            sorted_stack.append(self.stack.pop())

def test():
    stack = [1,3,7,4,5,6,77,2,3,45,6]
    ss = SortStack(stack)
    print ss.stack
    ss.sort()
    print ss.stack

if __name__ == "__main__":
    test()
