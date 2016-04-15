from classes.Node import *

class IsBalancedTree(object):
    def __init__(self):
        pass
    def is_balanced(self, root):
        if root == None:
            return True
        if abs(self.height(root.right) - self.height(root.left)) > 1:
            return False
        else:
            return self.is_balanced(root.right) and self.is_balanced(root.left)
    def height(self, root):
        if root == None:
            return 0
        if root.height == None:
            root.height = 1 + max(self.height(root.right), self.height(root.left))
        return root.height

def test():
    root = Node()
    root.right = Node()
    root.right.right = Node()
    root.right.right.right = Node()
    root.right.right.right.right = Node()
    root.right.left = Node()
    root.left = Node()
    root.left.right = Node()
    ibt = IsBalancedTree()
    print ibt.is_balanced(root)


if __name__ == "__main__":
    test()
