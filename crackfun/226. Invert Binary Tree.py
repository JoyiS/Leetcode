# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invertTreeHelper(root)
        return root

    def invertTreeHelper(self, root):
        if not root:
            return
        if root and (root.left or root.right):
            temp = root.left
            root.left = root.right
            root.right = temp
            root2 = root.left
            root1 = root.right
            self.invertTreeHelper(root2)
            self.invertTreeHelper(root1)
        else:
            return

# Iterative solution
class Solution(object):
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += [node.left, node.right]
        return root