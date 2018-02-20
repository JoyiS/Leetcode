'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = fast = slow = ListNode(0)
        dummy.next = fast.next = slow.next = head
        k = 0
        while fast and k < n + 1:
            fast = fast.next
            k += 1
        if k == n + 1:
            while fast:
                slow = slow.next
                fast = fast.next
        slow.next = slow.next.next
        return dummy.next

