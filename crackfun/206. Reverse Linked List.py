# Loop Method:
# http://algorithms.tutorialhorizon.com/reverse-a-linked-list/

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0)
        while head:
            nextNode = head.next
            head.next = prev.next
            prev.next = head
            head = nextNode
        return prev.next



# Recursion Method
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0)
        return self.doreverse(head, prev.next)

    def doreverse(self, head, newhead):
        if head == None:
            return newhead
        nextnode = head.next
        head.next = newhead
        return self.doreverse(nextnode, head)

