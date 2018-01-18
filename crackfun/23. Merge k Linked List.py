# https://leetcode.com/articles/merge-k-sorted-list/
# Method 1: (Brute Force): Convert Linked List to Array, Sort and put the output into one Linked List
# Method 2: (Priority Queue: Heap)
# Time Complexity (O(Nlogk)): N = total number of nodes, k number of linked lists
# Space Complexity (O())
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


# second time 1/17/2018

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        q = []
        dummy = output = ListNode(0)
        for node in lists:
            if node:
                heapq.heappush(q, (node.val, node))
        while q:
            (val, node) = heapq.heappop(q)
            output.next = node
            output = output.next
            if node.next:
                node = node.next
                heapq.heappush(q, (node.val, node))
        return dummy.next


# Method 3: Merge: Divide and Conquer:
# Time Complexity : Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.
# Space Complexity : O(1)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next