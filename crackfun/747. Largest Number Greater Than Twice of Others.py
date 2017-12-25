class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return -1
        first = nums[0]
        firstidx = 0
        second = -float('inf')
        secondidx = None
        for i in range(1, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                secondidx = firstidx
                firstidx = i
            elif nums[i] > second:
                second = nums[i]
                secondidx = i
        if first>=2*second:
            return firstidx
        else:
            return -1