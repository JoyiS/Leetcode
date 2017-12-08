# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.inorder(root, count)
        return count[k - 1]

    def inorder(self, node, count):
        if not node:
            return
        self.inorder(node.left, count)
        count.append(node.val)
        self.inorder(node.right, count)