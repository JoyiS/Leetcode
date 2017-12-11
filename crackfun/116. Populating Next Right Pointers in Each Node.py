# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        level = [root]
        while level:
            newlevel = []
            for node in level:
                if node.left:
                    newlevel += [node.left]
                if node.right:
                    newlevel += [node.right]

            for node, nextnode in zip(level[:-1], level[1:]):
                node.next = nextnode
            level[-1].next = None

            level = newlevel

# Method 2:
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        while root.left:  # One Layer to the next Layer
            cur = root.left
            prev = None
            while root:  # Move along one Layer from left to the right
                if prev: prev.next = root.left
                root.left.next = root.right
                prev = root.right
                root = root.next
            root = cur


