'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


class Codec:
    def serialize(self, root):
        preorder = ''
        if not root:
            preorder += ',None'
            return preorder
        preorder += ',' + str(root.val)
        preorder += self.serialize(root.left)
        preorder += self.serialize(root.right)
        return preorder

    def deserialize(self, encode_data):
        pos = -1
        data = encode_data[1:].split(',')
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = int(data[i])
        root, count = self.buildTree(data, pos)
        return root

    def buildTree(self, data, pos):
        pos += 1
        if pos >= len(data) or data[pos] == None:
            return None, pos

        root = TreeNode(data[pos])
        root.left, pos = self.buildTree(data, pos)
        root.right, pos = self.buildTree(data, pos)
        return root, pos

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


t = TreeNode(1)
tl = TreeNode(2)
tr = TreeNode(3)
t.left = tl
t.right = tr
trl = TreeNode(4)
trr = TreeNode(5)
trll = TreeNode(6)
trlr = TreeNode(7)
tr.left = trl
tr.right = trr
trl.left = trll
trl.right = trlr

'''
The preorder output:
    ',1,2,None,None,3,4,6,None,None,7,None,None,5,None,None'
'''