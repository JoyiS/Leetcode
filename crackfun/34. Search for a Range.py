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


# second time: 1/22/2018
'''
CORNER CASE: ARRAY [1], TARGET 1
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        while i<=j: # The equal sign is to take care of the corner case
            mid = (i+j)//2
            if nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j = mid-1
            else:
                left = mid-1
                while left>=0 and nums[left]==target:
                    left-=1
                while mid<len(nums) and nums[mid]==target:
                    mid+=1
                return [left+1,mid-1]
        return [-1,-1]