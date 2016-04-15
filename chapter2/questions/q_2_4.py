from classes.LinkedList import *


class DeviderHelper(object):
    def __init__(self, ll):
        self.ll = ll
    def devide_by(self, k):
        smaller = LinkedList()
        larger = LinkedList()
        current_node = ll.head
        while current_node:
            inserted_node = Node(current_node.val) # 参照渡すのを防ぐため。
            if current_node.val < k:
                last_smaller_node = inserted_node
                smaller.add_node(inserted_node)
            else:
                larger.add_node(inserted_node)
            current_node = current_node.next
        last_smaller_node.next = larger.head
        return smaller

ll = LinkedList()
ll.add_node(Node(3))
ll.add_node(Node(5))
ll.add_node(Node(4))
ll.add_node(Node(8))
ll.add_node(Node(6))
ll.add_node(Node(1))
dh = DeviderHelper(ll)
print 'Defo: ' + str(ll)
devided_ll = dh.devide_by(7)
print 'Result: ' + str(devided_ll)

# NOTE: Pythonでmutableなオブジェクトを渡している時は参照渡していると思って。
