'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        min1 = float('inf')
        min2 = float('inf')
        queue = [root]
        flag = 0
        while queue:
            newqueue = []
            for node in queue:
                if node.left:
                    newqueue += [node.left]
                if node.right:
                    newqueue += [node.right]
                if flag == 1 and node.val<min2 and node.val>min1:
                    min2 = node.val
                if node.val < min1:
                    flag = 1
                    min1 = node.val
            queue = newqueue
        return min2 if min2 != float('inf') else -1