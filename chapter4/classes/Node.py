class Node(object):
    def __init__(self, val=0, height=None, right=None, left=None):
        self.val = val
        self.height = height
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.val)
