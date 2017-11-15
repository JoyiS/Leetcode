class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = []
        ans = []
        self.helper(candidates, target, res, ans)
        return res

    def helper(self, candidates, target, res, ans):
        if target == 0:
            res.append([x for x in ans])
            return

        for i, elem in enumerate(candidates):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if elem <= target:
                ans.append(elem)
                self.helper(candidates[i + 1:], target - elem, res, ans)
                ans.pop()