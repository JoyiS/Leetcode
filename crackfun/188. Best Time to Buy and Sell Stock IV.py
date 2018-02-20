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