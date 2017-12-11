# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        alllevel = [[root.val]]
        while level:
            newlevel = []
            newlevelVal = []
            for node in level:
                if node.left:
                    newlevel.append(node.left)
                    newlevelVal += [node.left.val]
                if node.right:
                    newlevel.append(node.right)
                    newlevelVal += [node.right.val]
            level = newlevel
            if level:
                alllevel += [newlevelVal]
        i = 0
        for level in alllevel:
            if i % 2 == 1:
                level = level[::-1]
                alllevel = alllevel[:i] + [level] + alllevel[i + 1:]
            i += 1
        return alllevel