class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
        res = [[nums[0]]]
        for i in nums[1:]:
            news = [s[:j] + [i] + s[j:] for s in res for j in range(len(s) + 1)]
            res = news
        return res