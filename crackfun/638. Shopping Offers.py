class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.res = 0
        for idx, need in enumerate(needs):
            self.res += need * price[idx]
        if self.res == 0:
            return self.res
        self.dfs(price, special, needs, 0)

        return self.res

    def dfs(self, price, special, needs, money):
        flag = 0
        if needs == [0] * len(needs):
            self.res = min(self.res, money)
            return
        for s in special:
            for idx, need in enumerate(needs):
                if need - s[idx] < 0:
                    break
            else:
                flag = 1
                self.dfs(price, special, [need - s[idx] for idx, need in enumerate(needs)], money + s[-1])
        if flag == 0:
            for idx, need in enumerate(needs):
                if need > 0:
                    money += price[idx] * need
            self.res = min(self.res, money)
            return




