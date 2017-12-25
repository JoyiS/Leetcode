class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                j = k = mid
                while j >= 0 and nums[j] == target:
                    j -= 1
                while k < len(nums) and nums[k] == target:
                    k += 1
                return [j + 1, k - 1]
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return [-1, -1]
