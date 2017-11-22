# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.dfs(root, sum, path)
        return self.res

    def dfs(self, root, sum, path):
        if not root:
            return
        if root.val == sum and not root.left and not root.right:
            self.res.append(path + [root.val])
            return
        if root.left:
            self.dfs(root.left, sum - root.val, path + [root.val]) # Pay attention to the grammar here, not return
        if root.right:
            self.dfs(root.right, sum - root.val, path + [root.val])
