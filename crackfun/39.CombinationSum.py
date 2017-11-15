class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        ans = []
        self.dfs(ans, 0, candidates, target)
        return self.res

    def dfs(self, ans, idx, candidates, target):
        if target == 0:
            self.res.append(ans)
            return
        if target < 0:
            return
        for i in xrange(idx, len(candidates)):
            self.dfs(ans+[candidates[i]], i, candidates, target - candidates[i])  # Be very careful with the Grammar here that