# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        fast = fast.next
        while fast.next:
            while fast.next and fast.val != 9:
                fast = fast.next
                slow = slow.next
            if fast.val == 9:
                while fast.next and fast.val == 9:
                    fast = fast.next
                if fast.next:
                    slow = fast
                    fast = fast.next

        if fast.val != 9:
            fast.val += 1
            return dummy.next
        if fast.val == 9:
            slow.val += 1
            p = slow.next
            while p:
                p.val = 0
                p = p.next
            return dummy.next if slow != dummy else dummy # This is important