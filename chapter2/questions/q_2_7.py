from classes.LinkedList import *
from classes.Stack import *

class KaibunChecker(object):
    def __init__(self, ll):
        self.ll = ll

    def is_kaibun(self):
        self.__set_half_stack()
        return self.__stack_are_equal_to_list()

    def __set_half_stack(self):
        self.stack = Stack()
        slow_node = self.ll.head
        fast_node = self.ll.head
        while not self.__reach_end(fast_node):
            self.stack.push(self.__remove_haed())
            slow_node = self.ll.head
            fast_node = fast_node.next.next
        if self.__is_even_length(fast_node):
            self.stack.push(slow_node)
        self.__remove_haed()

    def __stack_are_equal_to_list(self):
        while not self.stack.isEmpty():
            node1 = self.stack.pop()
            node2 = self.__remove_haed()
            if node1.val != node2.val:
                return False
        if self.ll.head != None:
            raise Exception("Different length of stack and list!")
        return True

    def __remove_haed(self):
        node = self.ll.head
        self.ll.head = node.next
        return node

    def __reach_end(self, fast_node):
        if fast_node.next == None:
            return True
        elif fast_node.next.next == None:
            return True
        else:
            return False

    def __is_even_length(self, fast_node):
        if not self.__reach_end(fast_node):
            raise Exception("Don't use unless it reached end.")
        return fast_node.next != None


# Test

# ll = LinkedList()
# ll.add_node(Node(1))
# ll.add_node(Node(4))
# ll.add_node(Node(5))
# ll.add_node(Node(4))
# ll.add_node(Node(1))
# kc = KaibunChecker(ll)
# print kc.is_kaibun()
