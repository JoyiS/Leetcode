class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        oldtarget = None

        for i in range(len(nums) - 2):
            target = -nums[i]
            if target != oldtarget:
                oldj = None
                for j in range(i + 1, len(nums)):
                    if nums[j] != oldj:
                        s = nums[j + 1:]
                        if target - nums[j] in s:
                            res.append([nums[i], nums[j], target - nums[j]])
                            oldj = nums[j]
                oldtarget = target
        return res