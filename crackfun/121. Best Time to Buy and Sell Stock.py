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