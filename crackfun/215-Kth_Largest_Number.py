# Quick sort similar idea (O(n))
# if brute force sort and return -->O(logn)
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot

# 1/30/2018
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        large_nums, small_nums = [], []
        for x in nums:
            if x>pivot:
                large_nums.append(x)
            if x<pivot:
                small_nums.append(x)
        if len(large_nums)>=k:
            return self.findKthLargest(large_nums,k)
        if len(nums) - len(small_nums) < k :
            return self.findKthLargest(small_nums, k - (len(nums) - len(small_nums)))
        return pivot