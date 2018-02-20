# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This is a very good solution. From Geeks for Geeks.

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findMaxUtil(root):
            # Base Case
            if root is None:
                return 0

            # l and r store maximum path sum going through left
            # and right child of root respetively
            l = findMaxUtil(root.left)
            r = findMaxUtil(root.right)

            # Max path for parent call of root. This path
            # must include at most one child of root
            max_single = max(max(l, r) + root.val, root.val)

            # Max top represents the sum when the node under
            # consideration is the root of the maxSum path and
            # no ancestor of root are there in max sum path
            max_top = max(max_single, l + r + root.val)

            # Static variable to store the changes
            # Store the maximum result
            findMaxUtil.res = max(findMaxUtil.res, max_top)

            return max_single

        # Initialize result
        findMaxUtil.res = float("-inf")

        # Compute and return result
        findMaxUtil(root)
        return findMaxUtil.res

# 2/12/2018
class Solution(object):
    def maxPathSum(self, root):

        def maxSinglePath(root):
            if not root:
                return 0

            l = maxSinglePath(root.left)
            r = maxSinglePath(root.right)

            maxsingle = max(l + root.val, r + root.val, root.val)
            maxoverall = max(maxsingle, root.val + l + r)

            maxSinglePath.res = max(maxSinglePath.res, maxoverall)
            return maxsingle

        maxSinglePath.res = float('-inf')
        maxSinglePath(root)
        return maxSinglePath.res

