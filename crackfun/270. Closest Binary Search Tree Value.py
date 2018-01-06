'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        queue = [root]
        ret = [abs(root.val-target),root.val]
        while queue:
            node = queue.pop(0)
            if abs(node.val-target)<ret[0]:
                ret = [abs(node.val-target),node.val]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ret[1]