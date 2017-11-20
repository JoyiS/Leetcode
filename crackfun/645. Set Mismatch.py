class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.res = []
        n = len(nums)
        existmap = [False for i in range(0, n + 1)]
        for i in nums:
            if existmap[i] == False:
                existmap[i] = True
            else:
                self.res.append(i)
        for i in range(1, n + 1):
            if existmap[i] == False:
                self.res.append(i)
        return self.res

