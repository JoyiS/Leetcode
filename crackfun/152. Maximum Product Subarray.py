class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval = nums[0]
        maxval = nums[0]
        maximum = maxval
        for i in range(1,len(nums)):
            maxval,minval = max(nums[i],maxval*nums[i],minval*nums[i]), min(nums[i],maxval*nums[i],minval*nums[i])
            maximum = max(maxval,maximum)
        return maximum


# 1/21/2018
# second time
'''
the key point is that the subarray can depends on previous or not depending on that....
'''