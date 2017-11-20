# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or head.next == None:
            return head

        lenp = head
        length = 0
        while lenp != None:
            lenp = lenp.next
            length += 1

        k = k % length
        if k == 0:
            return head

        p = q = head
        i = 0
        while i < k:
            q = q.next
            i += 1

        while q.next != None:
            p = p.next
            q = q.next

        temp = p.next # Remember to get the next first!!
        p.next = None
        q.next = head
        return temp