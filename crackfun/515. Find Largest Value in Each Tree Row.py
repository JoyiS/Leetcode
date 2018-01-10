# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        queue = [[root, 0]]
        curr_depth = 0
        levelmax = root.val
        res = []

        for node, depth in queue:
            if node:
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
                if curr_depth != depth:
                    curr_depth = depth
                    res.append(levelmax)
                    levelmax = float('-inf')
                levelmax = max(node.val, levelmax)
        res += [levelmax]
        return res
