class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = float('inf')
        maxNum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]>0:
                minNum = min(minNum, nums[i])
                maxNum = max(maxNum, nums[i])
                count+=1
        if minNum>1:
            return 1
        for i in range(minNum, maxNum+2):
            if i not in nums:
                return i