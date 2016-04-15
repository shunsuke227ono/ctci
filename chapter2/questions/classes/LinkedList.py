class LinkedList(object):
    @classmethod
    def test(cls):
        print "test"
    def __init__(self, node = None):
        self.head = node # first node!
        self.tail = node
    def __str__(self):
        if self.head == None:
            return "LinkedList []"
        i = self.head
        node_store = [str(i.val)]
        while i.next != None:
            i = i.next
            node_store.append(str(i.val))
        return "LinkedList [ " + "->".join(node_store) + " ]"
    def add_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def remove_val(self, val):
        if self.head.val == val:
            self.head = self.head.next
        else:
            current = self.head
            while(current.next != None):
                if current.next == val:
                    current.next = current.next.next
                    break
                else:
                    current = current.next
    def remove_duplicate1(self):
        # O(n)
        if self.head == None:
            return
        current = self.head
        val_exist = {current.val: True}
        while(current.next):
            print current.next
            if current.next.val in val_exist.keys():
                current.next = current.next.next
            else:
                val_exist[current.next.val] = True
                current = current.next
    def remove_duplicate2(self):
        # O(n^2)
        if self.head == None:
            return
        current = self.head
        while current:
            runner = current
            while runner.next:
                if current.val == runner.next.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
    def number_to_end(self, node):
        if not node:
            return 0
        elif not node.next:
            return 1
        else:
            return self.number_to_end(node.next) + 1
    def nth_to_end1(self, n):
        # O(n^2)
        current = self.head
        while(current):
            if self.number_to_end(current) == n:
                return current
            current = current.next
        return -1
    def nth_to_end2(self, n, node):
        # O(n), Memory O(n)
        if not node:
            return 0
        elif not node.next:
            return 1
        else:
            k = self.nth_to_end2(n, node.next) + 1
            if k == n:
                print "result: " + str(node)
            return k
    def nth_to_end3(self, n):
        # O(n), Memory O(1)
        current = self.head
        runner = self.nth_node(n)
        if runner == -1:
            return -1
        else:
            while runner:
                runner = runner.next
                current = current.next
            return current

    def nth_node(self, n):
        if not self.head:
            return -1
        current = self.head
        runner = current
        for i in range(n):
            runner = runner.next
            if not runner:
                return -1
        return runner


# Test

# LinkedList.test()
# ll = LinkedList()
# ll.add_node(Node(3))
# ll.add_node(Node(3))
# ll.add_node(Node(3))
# ll.add_node(Node(4))
# ll.add_node(Node(1))
# ll.add_node(Node(4))
# ll.add_node(Node(1))
# print str(ll.nth_to_end1(2))
# print str(ll.nth_to_end2(2, ll.head))
# print str(ll.nth_to_end3(2))
# print str(ll)
# ll.remove_duplicate2()
# print str(ll)
# ll.remove_duplicate2()
# print str(ll)
