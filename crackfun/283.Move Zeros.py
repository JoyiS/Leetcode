class Solution(object):
    def moveZeroes(self, nums):
        zero = 0  # records the position of potential "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

# 1/29/2018

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroIdx = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[zeroIdx] = nums[zeroIdx], nums[i]
                zeroIdx += 1
