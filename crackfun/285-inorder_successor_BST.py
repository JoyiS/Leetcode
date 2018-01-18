# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeftMost(self, node):
        if node == None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def findNextParent(self, node):
        if node == None:
            return None
        temp = node
        if temp.parent is not None:
            p = temp.parent
        else:
            p = None
        while p and p.left is not temp:
            p = p.parent
            temp = temp.parent
        return p

    def findNextParent2(self, root, node):
        parent = []
        while root and root!=node:
            if root.val > node.val:
                parent = root
                root = root.left
            else:
                root = root.right
        return parent

    def next(self, root, node):
        if node == None:
            return None
        if node.right is not None:
            self.findLeftMost(node.right)
        else:
            self.findNextParent2(node)

'''
# second time.. I get it
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            return self.leftmost(root, p.right)
        else:
            return self.nextparent(root, p)

    def leftmost(self, root, p):
        while p.left:
            p = p.left
        return p

    def nextparent(self, root, p):
        parent = None
        while root and root.val != p.val:
            if p.val > root.val:
                root = root.right
            else:
                parent = root
                root = root.left
        return parent




