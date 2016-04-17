class IsSubtree(object):
    def __init__(self):
        pass
    def sub_tree(root, sub_root):
        if root == None:
            return False
        if root.val == sub_root.val:
            if self.match_tree(root, sub_root):
                return True
        return self.sub_tree(root.right, sub_root) or self.sub_tree(root.left, sub_root)
    def match_tree(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.match_tree(root1.right, root2.right) and self.match_tree(root1.left, root2.left)
