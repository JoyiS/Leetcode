# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h=0
        if root.left or root.right:
            h+=1
            return h+max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 1