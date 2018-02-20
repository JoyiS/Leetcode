# My method O(n)
# Get inspired from the get k th largest in an array problem.
# DIVIDE citations into three regions, x<h; x==h and x>h
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        minh = min(min(citations), len(citations))
        maxh = min(max(citations), len(citations))
        n = len(citations)
        hs = minh
        for h in range(minh, maxh + 1):
            count = 0
            for i in citations:
                if i < h:
                    count += 1
            if n - count < h:
                break
            if n - count >= h:
                hs = h
        return hs

# Method 2: nlog(n) : sort
class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n - i):
                return n - i
        return 0


