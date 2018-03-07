class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if k == 0:
            return 0
        buypoint = []
        sellpoint = []
        if prices[1] > prices[0]:
            buypoint.append(0)
        for i in range(1, len(prices) - 1):
            if prices[i] - prices[i - 1] <= 0 and prices[i + 1] - prices[i] > 0:
                buypoint.append(i)
            if prices[i] - prices[i - 1] > 0 and prices[i + 1] - prices[i] <= 0:
                sellpoint.append(i)
        if prices[-1] > prices[-2]:
            sellpoint.append(len(prices) - 1)

        earn = []
        for i, j in zip(buypoint, sellpoint):
            earn.append(prices[j] - prices[i])

        res = sum(earn)
        if len(buypoint) <= k:
            return res

        sacrifice = []
        for i, j in zip(sellpoint[:-1], buypoint[1:]):
            sacrifice.append(prices[i] - prices[j])
        final = sorted(earn + sacrifice)
        rd = len(earn) - k
        return res - sum(final[:rd])

'''
DP 
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        T = [[[0, 0] for kk in range(k + 1)] for i in range(len(prices) + 1)]
        INF = float('inf')
        for i in range(len(prices) + 1):
            for kk in range(k + 1):
                T[0][kk][0] = 0
                T[0][kk][1] = -INF
                T[i][0][0] = 0
                T[i][0][1] = -INF
                if i > 0:
                    T[i][kk][0] = max(T[i - 1][kk][0], T[i - 1][kk][1] + prices[i - 1])
                    T[i][kk][1] = max(T[i - 1][kk][1], T[i - 1][kk - 1][0] - prices[i - 1])
        return T[len(prices)][k][0]

