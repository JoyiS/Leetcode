class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

    def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        l = head # I made a mistake here by setting l = head.next
        if not l1 and not l2:
            return head.next
        if not l1:
            l.next = l2
        if not l2:
            l.next = l1
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        if not l1:
            l.next = l2
        else:
            l.next = l1
        return head.next
