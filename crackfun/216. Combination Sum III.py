class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.k = k
        self.res = []
        ans = []
        self.dfs(n, ans, 0)
        return self.res

    def dfs(self, n, ans, i):
        if len(ans) == self.k and n == 0:
            self.res.append([x for x in ans])
            return
        if len(ans) > self.k or n < 0:
            return

        for j in range(i + 1, min(n + 1, 10)):
            ans.append(j)
            self.dfs(n - j, ans, j)
            ans.pop()