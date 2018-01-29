class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        last = None
        for i in range(len(nums)):
            if nums[i] != last:
                last = nums[i]
                newtarget = 0-nums[i]
                d = {}
                lastj = None
                for j in range(i+1,len(nums)):
                    if nums[j] != lastj:
                        if nums[j] in d:
                            res += [[nums[i],newtarget - nums[j], nums[j]]]
                            lastj = nums[j]
                        else:
                            d[newtarget - nums[j]] = j
        return res