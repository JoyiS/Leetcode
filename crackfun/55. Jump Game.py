class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        i = 0
        while i<=maxpos and i<len(nums):
            maxpos = max(maxpos, i+nums[i])
            if i+nums[i]>=len(nums)-1:
                return True
            i+=1
        return False

# TLE???!!!
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        if nums[0] == 0:
            return False
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            if i<=dp[i]:
                if i+nums[i]>len(nums):
                    return True
                dp[i] = max(dp[i],i+nums[i])
        return False
