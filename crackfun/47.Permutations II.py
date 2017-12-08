class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        s = [[nums[0]]]
        i = 1
        while i < len(nums):
            news = []
            for s0 in s:
                for j in range(len(s0) + 1):
                    news.append(s0[:j] + [nums[i]] + s0[j:])
                    if j < len(s0) and s0[j] == nums[i]: # avoid insert before its duplicates
                        #print(news[-1])
                        #print(s0,j)
                        break
            s = news
            i += 1
        return s



