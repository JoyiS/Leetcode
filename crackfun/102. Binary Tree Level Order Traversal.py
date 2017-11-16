# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        level = [root]
        res = []
        while level:
            res.append([x.val for x in level])
            newlevel = []
            for node in level:
                if node and node.left is not None:
                    newlevel.append(node.left)
                if node and node.right is not None:
                    newlevel.append(node.right)
            level = newlevel
        return res