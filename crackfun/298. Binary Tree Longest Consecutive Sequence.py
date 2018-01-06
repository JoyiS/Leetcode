def longestConsecutive(root):
    if not root:
        return 0

    ret = 0
    stack = [(root, 1)]
    while stack:
        node, cnt = stack.pop()
        if node.left:
            stack.append((node.left, cnt + 1 if node.left.val == node.val + 1 else 1))
        if node.right:
            stack.append((node.right, cnt + 1 if node.right.val == node.val + 1 else 1))
        ret = max(ret, cnt)

    return ret

# Time:  O(n)
# Space: O(h)

# This is a typical recursion problem.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def longestConsecutiveHelper(root):
            if not root:
                return 0

            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)

            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1)
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len, left_len, right_len)

            return cur_len

        longestConsecutiveHelper(root)
        return self.max_len


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# The soltuion below gives memory limit exceeds
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlen = 0
        self.dfs(root, [])
        return self.maxlen

    def dfs(self, node, path):
        if not node:
            return
        if not path or path[-1] + 1 == node.val:
            self.maxlen = max(self.maxlen, len(path)+1)
            self.dfs(node.left, path+[node.val])
            self.dfs(node.right, path+[node.val])
        else:
            self.maxlen = max(self.maxlen, 1)
            self.dfs(node.left, [node.val])
            self.dfs(node.right,[node.val])



