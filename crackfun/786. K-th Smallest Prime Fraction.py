class Solution(object):
    import heapq
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        q = []
        for i in range(len(A) - 1, -1, -1):
            for j in range(i):
                val = float(A[j]) / float(A[i])
                if len(q) < K or q[K - 1][0] > val:
                    heapq.heappush(q, (val, [A[j], A[i]]))
                else:
                    break

        for i in range(K):
            val, res = heapq.heappop(q)
        return res