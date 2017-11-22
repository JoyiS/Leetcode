# Method 1: Do it all and return the minDepth
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        depth = 0
        self.godown(root, depth)
        return min(self.res)

    def godown(self, root, depth):
        if not root:
            self.res.append(depth)
            return
        if root.left:
            self.godown(root.left, depth + 1)
        if root.right:
            self.godown(root.right, depth + 1)
        if not root.left and not root.right:
            self.res.append(depth + 1)
            return

# Method 2:
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
