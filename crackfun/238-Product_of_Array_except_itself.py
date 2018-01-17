class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        output = []
        # construct L to R product

        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        # construct R to L
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


