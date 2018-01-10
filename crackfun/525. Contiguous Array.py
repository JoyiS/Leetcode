class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        d = {}
        d[0] = -1
        sumi = [nums[0]]
        d[nums[0]] = 0
        for i in range(1, len(nums)):
            sumi += [sumi[i - 1] + nums[i]]
            if sumi[i] not in d:
                d[sumi[i]] = i
            else:
                res = max(res, i - d[sumi[i]])
        return res