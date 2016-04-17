from classes.Node import *

class CommonAncestor(object):
    def __init__(self):
        pass
    def find_anc(self, root, node1, node2):
        if root == node1 or root == node2:
            return False
        if not self.__has(root, node1) or not self.__has(root, node2):
            return False
        has_right_node1 = self.__has(root.right, node1)
        has_right_node2 = self.__has(root.right, node2)
        if has_right_node1 != has_right_node2:
            return root
        if has_right_node1 and has_right_node2:
            return self.find_anc(root.right, node1, node2)
        if not has_right_node1 and not has_right_node2:
            return self.find_anc(root.left, node1, node2)
        raise Exception
    def __has(self, root, node):
        if root == node:
            return True
        if root == None:
            return False
        return self.__has(root.right, node) or self.__has(root.left, node)

    def find_anc_better(self, root, node1, node2):
        if not self.__has(root, node1) or not self.__has(root, node2):
            raise Exception
        return self.common_ancestor(root, node1, node2)

    def common_ancestor(self, root, node1, node2):
        if root == None:
            return None
        if root == node1 and root == node2:
            return root

        x = self.common_ancestor(root.left, node1, node2)
        # Find CommonAncestor under root.left
        if x != None and x != node1 and x != node2:
            return x

        y = self.common_ancestor(root.right, node1, node2)
        # Find CommonAncestor under root.right
        if y != None and y != node1 and y != node2:
            return y

        # (x == node1 and y == node2) or (x == node2 and y == node1)
        if x != None and y != None:
            return root

        # if root == one of node1,2, x or y be none.
        if root == node1 or root == node2:
            return root

        return x == None ? y : x


def test():
    root = Node(val=1)
    root.right = Node(val=2)
    root.right.right = Node(val=3)
    node1 = Node(val=4)
    root.right.right.right = node1
    root.right.right.right.right = Node(val=5)
    node2 = Node(val=6)
    root.right.left = node2
    root.left = Node(val=7)
    node3 = Node(8)
    root.left.right = node3
    cm = CommonAncestor()
    print cm.find_anc(root, node1, node3).val

if __name__ == "__main__":
    test()
