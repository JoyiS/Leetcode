class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        last = prices[0]
        d = 0
        for i in range(1, len(prices)):
            if prices[i] > last:
                d += prices[i] - last
            last = prices[i]

        return d