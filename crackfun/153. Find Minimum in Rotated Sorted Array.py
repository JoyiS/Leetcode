class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = int((l + r) / 2)
            if mid == r or mid == l:
                return min(nums[l], nums[r])
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
