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
        lastvals = []
        l = l.next
        while l:
            if l.val == last:
                lastvals.append(last)
                l = l.next
                p.next = l
            else:
                last = l.val
                l = l.next
                p = p.next

        while head and head.val in lastvals:
            head = head.next
        if not head or head.next == None:
            return head
        pp = ll = head
        ll = ll.next
        while ll:
            if ll.val in lastvals:
                ll = ll.next
                pp.next = ll
            else:
                ll = ll.next
                pp = pp.next
        return head