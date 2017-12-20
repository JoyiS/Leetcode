# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output = []
        self.preorderThelper(root)

        return self.output

    def preorderThelper(self, root):
        if not root:
            return
        self.output += [root.val]
        self.preorderThelper(root.left)
        self.preorderThelper(root.right)

# There are iterative methods. To check

