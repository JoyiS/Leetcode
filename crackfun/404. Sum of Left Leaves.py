# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(0, root)]
        res = 0
        while queue:
            (left, node) = queue.pop(0)
            if left and not node.left and not node.right:
                res += node.val
            if node.left:
                queue += [(1,node.left)]
            if node.right:
                queue += [(0,node.right)]
        return res