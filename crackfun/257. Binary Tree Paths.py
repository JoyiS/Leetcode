# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.res = []
        self.helper(str(root.val), root)
        return self.res

    def helper(self, path, node):
        if not node.left and not node.right:
            self.res += [path]
            return
        if node.left:
            self.helper(path + '->' + str(node.left.val), node.left)
        if node.right:
            self.helper(path + '->' + str(node.right.val), node.right)