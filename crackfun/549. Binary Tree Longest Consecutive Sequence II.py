# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This question is great:
'''
我的思想进阶：
（1） dfs 或者 我写的helper function可以一次性返回 ascending的path length，以及descending的path length。
这样避免重复计算，节省计算时间。
（2） 理解返回值，返回的是从当前这一点往下数得到的path的长度。
（3） 和之前的124题类似，考虑四种情况： 只有node， node + left， node + right， node + both left and right.
(4) 保持全局变量来考虑这四种情况的max
'''

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0, 0

        root_left_asc, root_left_dsc = self.helper(root.left)
        root_right_asc, root_right_dsc = self.helper(root.right)

        max_asc, max_dsc = 1, 1
        if root.left:
            if root.left.val == root.val + 1:
                max_asc = max(max_asc, 1 + root_left_asc)
            elif root.left.val == root.val - 1:
                max_dsc = max(max_dsc, 1 + root_left_dsc)

        if root.right:
            if root.right.val == root.val + 1:
                max_asc = max(max_asc, 1 + root_right_asc)
            elif root.right.val == root.val - 1:
                max_dsc = max(max_dsc, 1 + root_right_dsc)

        if root.left and root.right:
            if root.left.val == root.val - 1 and root.right.val == root.val + 1:
                self.res = max(self.res, root_left_dsc + root_right_asc + 1)
            if root.left.val == root.val + 1 and root.right.val == root.val - 1:
                self.res = max(self.res, root_left_asc + root_right_dsc + 1)

        self.res = max(self.res, max_asc, max_dsc)

        return max_asc, max_dsc

# DFS
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l[0] = max(l[0], li + rd + 1, ld + ri + 1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        l = [0]
        dfs(root, root)
        return l[0]