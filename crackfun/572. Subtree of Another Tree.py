# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        queue = [s]
        while queue:
            node = queue.pop(0)
            if node.val == t.val:
                if self.isSameTree(node, t):
                    return True
            if node.left:
                queue += [node.left]
            if node.right:
                queue += [node.right]
        return False

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
