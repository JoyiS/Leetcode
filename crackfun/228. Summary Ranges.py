class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        last = nums[0] + 1
        lastNode = nums[0]
        res = []

        for i in range(1, len(nums)):
            if nums[i] != last:
                if last - lastNode == 1:
                    line = str(lastNode)
                else:
                    line = str(lastNode) + '->' + str(last - 1)
                res += [line]
                lastNode = nums[i]
            last = nums[i] + 1

        if last - lastNode == 1:
            line = str(lastNode)
        else:
            line = str(lastNode) + '->' + str(last - 1)
        res += [line]

        return res
