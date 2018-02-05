class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<2:
            return [nums]
        s = [[nums[0]]]
        i=1
        while i<len(nums):
            news = []
            for s0 in s:
                for j in range(len(s0)+1):
                    news.append(s0[:j]+[nums[i]]+s0[j:])
            s = news
            i+=1
        return s

# 2/4/2017
class Solution:
    def permute(self, nums):
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            res = [a[:j] + [nums[i]] + a[j:] for a in res for j in range(len(a)+1)]
        return res