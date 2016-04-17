class NextNode(object):
    def __init__(self):
        pass
    def get_next(self, node):
        if node.right != None:
            return self.most_left_node(node.right)
        elif node.parent != None:
            while node.parent != None and node == node.parent.right:
                node = node.parent
            return node.parent
        else:
            return None

def test():
    nn = NextNode()
    nn.get_next()
