'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ret = []
        queue = [root]
        while queue:
            node = queue.pop()
            ret += [(abs(node.val- target),node.val)]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.sort(key = lambda x:x[0])
        return [x[1] for x in ret][:k]

#--------------------------other people solution
class Solution(object):
    def closestKValues(self, root, target, k):
        def less_equal(root):
            if root:
                if root.val <= target:
                    for v in less_equal(root.right): yield v
                    yield target - root.val, root.val
                for v in less_equal(root.left): yield v

        def greater(root):
            if root:
                if root.val > target:
                    for v in greater(root.left): yield v
                    yield root.val - target, root.val
                for v in greater(root.right): yield v

        le, gr = less_equal(root), greater(root)
        merged = heapq.merge(le, gr)
        return [next(merged)[1] for _ in range(k)]



