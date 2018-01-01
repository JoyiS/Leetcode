# A very interesting question:
#(1) A1->A2->* and B1->B2->*
#(2) a and b has different length
#(3) a and b does not share common node
# Three different condition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            A, B = headA, headB
            while A != B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A
