""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def helper(root, lower, upper):
    if root == None:
        return True
    if root.data >= upper or root.data <= lower:
        return False
    return helper(root.left, lower, root.data) and helper(root.right, root.data, upper)

def checkBST(root):
    return helper(root, -float('inf'), float('inf'))
