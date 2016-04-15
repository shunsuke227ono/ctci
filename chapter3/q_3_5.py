from classes.Node import *

class MyQueue(object):
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    def enqueue(self, val):
        self.input_stack.append(val)
    def dequeue(self):
        if len(self.output_stack) == 0:
            while len(self.input_stack) > 0:
                self.output_stack.append(self.input_stack.pop())
        if len(self.output_stack) == 0:
            return None
        return self.output_stack.pop()
    def __str__(self):
        nodes =  self.output_stack[::-1] + self.input_stack
        return str(nodes)

def test():
    mq = MyQueue()
    mq.enqueue(1)
    mq.enqueue(4)
    mq.enqueue(3)
    mq.enqueue(2)
    print mq
    print mq.dequeue()
    print mq
    mq.enqueue(9)
    print mq
    print mq.dequeue()
    mq.enqueue(4)
    print mq
    print mq.dequeue()
    mq.enqueue(7)
    print mq

if __name__ == "__main__":
    test()
