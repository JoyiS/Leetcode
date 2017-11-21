# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.comp(root.left, root.right)
        else:
            return True

    def comp(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.comp(p.left, q.right) and self.comp(p.right, q.left)
        else:
            return False
