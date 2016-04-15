from classes.Stack import *

class HanoiProblem(object):
    def __init__(self, n):
        stack0 = range(n)
        stack0.reverse()
        stack1 = []
        stack2 = []
        self.n = n
        self.stacks = [stack0, stack1, stack2]
    def move(self, n, r, d, b):
        self.__check_input(n, r, d, b)
        if n == 0:
            return
        self.move(n-1, r, b, d)
        self.__move_base(r, d)
        self.move(n-1, b, d, r)
        self.__print_current_state()
        return
    def __check_input(self, n, r, d, b):
        if n > self.n:
            raise Exception("wrong input. n is too large")
        if not( 0 in [r,d,b] and 1 in [r,d,b] and 2 in [r,d,b] ):
            raise Exception("wrong input. r, d, b should be combination of [1,2,3]")
    def __move_base(self, r, d):
        base = self.stacks[r].pop()
        self.stacks[d].append(base)
    def __print_current_state(self):
        print "stack0: " + str(self.stacks[0]) + "\n"
        print "stack1: " + str(self.stacks[1]) + "\n"
        print "stack2: " + str(self.stacks[2]) + "\n"

#-----------------test-------------------
def test():
    hp = HanoiProblem(3)
    hp.move(3, 0, 2, 1)

if __name__ == "__main__":
    test()
