class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            minp = prices[0]
            d = [0]
            for p in prices:
                if p < minp:
                    minp = p
                d.append(max(p-minp, d[-1]))
            return d[-1]
        else:
            return 0

# 1/28/2018
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        minv = prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] - minv > dp[i - 1]:
                dp[i] = prices[i] - minv
            else:
                dp[i] = dp[i - 1]
            if prices[i] < minv:
                minv = prices[i]

        return dp[-1]