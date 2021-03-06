# DP version
# Transition state function and initial states
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount  # initialization
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        return [dp[amount], -1][dp[amount] == MAX]

# BFS version
# for BFS method in this type of question, it is important to have a visited status flag and disregard solutions when the same point has been visited in previous level
# This can effectively accelerate the process
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        v = [None] * (amount + 1)
        v[0] = [1]
        level = [amount]
        levelnum = 0
        while level:
            levelnum += 1
            newlevel = []
            for val in level:
                for c in coins:
                    if val - c == 0:
                        return levelnum
                    if val - c > 0:
                        if not v[val - c]:
                            v[val - c] = 1
                            newlevel += [val - c]
                    else:
                        continue
            level = newlevel
        return -1


#-------------------------
# Bottom Up
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [MAX]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in range(len(coins)):
                if i >= coins[c]:
                    dp[i] = min(1+dp[i-coins[c]],dp[i])

        return [dp[amount], -1][dp[amount]==MAX]

# Top Down
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        dp = [0] * (amount + 1)
        return self.helper(coins, amount, dp)

    def helper(self, coins, amount, dp):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if dp[amount]:
            return dp[amount]
        MAX = float('inf')
        for c in coins:
            res = self.helper(coins, amount - c, dp)
            if 0 <= res < MAX:
                MAX = 1 + res
        dp[amount] = -1 if MAX == float('inf') else MAX
        return dp[amount]

