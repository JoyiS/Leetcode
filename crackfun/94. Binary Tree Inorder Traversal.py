# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.outputs = []
        self.inOrder(root, self.outputs)
        return self.outputs

    def inOrder(self, root, outputs):
        if root is None:
            return None
        self.inOrder(root.left, outputs)
        outputs.append(root.val)
        self.inOrder(root.right, outputs)