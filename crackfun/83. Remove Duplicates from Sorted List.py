# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        p = l = head
        last = l.val
        l = l.next
        while l:
            if l.val == last:
                l = l.next
                p.next = l
            else:
                last = l.val
                l = l.next
                p = p.next
        return head
