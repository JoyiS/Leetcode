class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return a