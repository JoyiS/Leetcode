'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
          1
         / \
        2   3
       / \
      4   5
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2
2. Now removing the leaf [2] would result in this tree:

          1
3. Now removing the leaf [1] would result in the empty tree:

          []
Returns [4, 5, 3], [2], [1].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = {}
        self.node = {}
        self.helper(root)
        allres = []

        for nodes, height in zip(self.node.values(), self.node.keys()):
            res = []
            for node in nodes:
                res += [node.val]
                if node.left:
                    node.left = None
                if node.right:
                    node.right = None
            allres += [res]
        return allres

    def helper(self, root):
        if root in self.d:
            return self.d[root]
        if not root:
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            height = max(left, right) + 1
            self.d[root] = height
            if height in self.node:
                self.node[height] += [root]
            else:
                self.node[height] = [root]
            return height
