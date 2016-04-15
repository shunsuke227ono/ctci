from classes.LinkedList import *

class AdditonHelper(object):
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def add1(self):
        # say list's head is smallest digit
        carrie = 0
        current_node1 = l1.head
        current_node2 = l2.head

        res = LinkedList()
        while current_node1 or current_node2:
            val1 = current_node1.val if current_node1 else 0
            val2 = current_node2.val if current_node2 else 0

            sum_result = val1 + val2 + carrie
            carrie = sum_result // 10
            number = sum_result % 10
            res.add_node(Node(number))

            current_node1 = current_node1.next if current_node1 else None
            current_node2 = current_node2.next if current_node2 else None
        return res

    def add2(self):
        # say list's head is largest digit
        self.res = LinkedList()
        self.__compensate_zeros_to_shorter()
        self.__add_recursively(self.l1.head, self.l2.head)
        return self.res

    def __add_recursively(self, node1, node2):
        val1 = node1.val
        val2 = node2.val
        if bool(node1) != bool(node2):
            raise Exception('Different length lists!')
        if node1.next == None and node2.next == None:
            sum_res = val1 + val2
        else:
            sum_res = val1 + val2 + self.__add_recursively(node1.next, node2.next)
        number = sum_res % 10
        self.res.add_node(Node(number))
        carrie = sum_res // 10
        return carrie

    def __compensate_zeros_to_shorter(self):
        self.__set_shorter_and_longer()
        for i in range(self.diff):
            node = Node(0)
            node.next = self.shorter_list.head
            self.shorter_list.head = node

    def __set_shorter_and_longer(self):
        current_node1 = self.l1.head
        current_node2 = self.l2.head
        self.diff = 0
        while current_node1 or current_node2:
            if bool(current_node1) != bool(current_node2):
                self.shorter_list = self.l2 if current_node1 else self.l1
                self.diff += 1
            current_node1 = current_node1.next if current_node1 else None
            current_node2 = current_node2.next if current_node2 else None
        if self.diff == 0:
            self.shorter_list = self.l1

l1 = LinkedList()
l1.add_node(Node(7))
l1.add_node(Node(3))
l1.add_node(Node(6))
l1.add_node(Node(8))

l2 = LinkedList()
l2.add_node(Node(6))
l2.add_node(Node(2))

ah = AdditonHelper(l1, l2)
res = ah.add2()
print res
