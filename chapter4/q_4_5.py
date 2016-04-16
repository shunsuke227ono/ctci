import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class CreateBST(object):
    def __init__(self, sorted_list):
        self.sorted_list = sorted_list
    def create_bst(self, start_index, end_index):
        if start_index > end_index:
            return None
        root_index = (start_index + end_index) / 2
        root = Node(self.sorted_list[root_index])
        root.right = self.create_bst(root_index+1, end_index)
        root.left = self.create_bst(start_index, root_index-1)
        self.print_tree(root)
        return root
    def print_tree(self, root):
        values = []
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            values.append(node.value)
            if node.right != None:
                q.put(node.right)
            if node.left != None:
                q.put(node.left)
        print values


class IsBST(object):
    def __init__(self):
        self.current = None
        pass
    def is_bst(self):
        pass
    def check_in_order(self, root):
        if root == None:
            return True
        if not self.check_in_order(root.left):
            return False

        if self.current == None:
            self.current = root.value
            print self.current
        elif root.value >= self.current:
            self.current = root.value
            print self.current
        else:
            return False

        if not self.check_in_order(root.right):
            return False

        return True

    def check_min_max(self):
        pass

def test():
    sorted_list = [1,2,3,4,5,5,6,6,7,8,8,10,100,1000]
    cbst = CreateBST(sorted_list)
    root = cbst.create_bst(0, len(sorted_list)-1)
    cbst.print_tree(root)
    print root
    ibst = IsBST()
    print ibst.check_in_order(root)

if __name__ == "__main__":
    test()
