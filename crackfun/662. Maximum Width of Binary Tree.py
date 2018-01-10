# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
class Solution(object):
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
                #print(ans)
        return ans

# DFS
class Solution(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos) # what is the set default
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans

    #   setdefault(key[, default])
    #   If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

# TLE
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        width = 1
        preval = ''
        while queue:
            level = []
            xval = ''
            val = ''
            for node in queue:
                if node.left:
                    level.append(node.left)
                    xval += '1'
                if not node.left:
                    xval += '0'
                if node.right:
                    level.append(node.right)
                    xval += '1'
                if not node.right:
                    xval += '0'
            if preval:
                for x in preval:
                    if x=='0':
                        val+='00'
                    if x=='1':
                        val += xval[:2]
                        xval = xval[2:]
            else:
                val = xval
            if '1' in val:
                currwidth = (len(val) - val[::-1].find('1', 0) - val.find('1', 0))
                width = max(width, currwidth)
            else:
                return width
            preval = val
            queue = level
