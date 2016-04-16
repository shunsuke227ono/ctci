from classes.LinkedList import *

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = None

class TreeToList(object):
    def __init__(self, root):
        self.root = root
        self.lists = {}
    def create_lists_and_get_height(self, root):
        if root == None:
            return 0
        if root.height != None:
            return height
        else:
            root.height = max(self.create_lists_and_get_height(root.left), self.create_lists_and_get_height(root.right)) + 1

        if not root.height in self.lists:
            self.lists[root.height] = LinkedList()

        self.lists[root.height].add_node(Node(root.value))
        return root.height

def test():
    root = TreeNode(10)
    root.right = TreeNode(4)
    root.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    ttl = TreeToList(root)
    ttl.create_lists_and_get_height(root)
    for key, value in ttl.lists.iteritems():
        print key
        print value

if __name__ == "__main__":
    test()
