class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = [0]
        for i in range(len(nums) - 1):
            self.dp.append(self.dp[-1] + self.nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
            self.sumRange(j, i)
        return self.dp[j] - self.dp[i] + self.nums[j]


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)