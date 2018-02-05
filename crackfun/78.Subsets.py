
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = [[]]
        for i in range(len(nums)):
            s += [a+[nums[i]] for a in s]
        return s