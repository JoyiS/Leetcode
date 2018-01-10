# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 想清楚了再开始写
# This is a very good bottom up question.
# if print seen: the output will be a bottom up (from leaves to the root)
class Solution(object):
    def checkEqualTree(self, root):
        seen = [] # global variable

        def sum_(node):
            if not node: return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen


# BAD TLE from Joy...:)
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        self.res = []
        if root.left and root.right:
            rootval = root.val + self.helper(root.left) + self.helper(root.right)
        elif root.left:
            rootval = root.val + self.helper(root.left)
        elif root.right:
            rootval = root.val + self.helper(root.right)
        else:
            return False

        # print(self.res)
        for i in range(len(self.res)):
            if rootval == 2 * self.res[i]:
                return True
        return False

    def helper(self, root):
        if root.left and root.right:
            self.res += [root.val + self.helper(root.left) + self.helper(root.right)]
            return root.val + self.helper(root.left) + self.helper(root.right)
        elif root.left:
            self.res += [root.val + self.helper(root.left)]
            return root.val + self.helper(root.left)
        elif root.right:
            self.res += [root.val + self.helper(root.right)]
            return root.val + self.helper(root.right)
        else:
            self.res += [root.val]
            return root.val
