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

def test():
    sorted_list = [1,2,3,4,5,5,6,6,7,8,8,10,100,1000]
    cbst = CreateBST(sorted_list)
    cbst.print_tree(cbst.create_bst(0, len(sorted_list)-1))


if __name__ == "__main__":
    test()
