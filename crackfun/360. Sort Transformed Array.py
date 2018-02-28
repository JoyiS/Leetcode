# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x, a, b, c : a * x * x + b * x + c

        result = []
        if not nums:
            return result

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            if d * f(nums[left], a, b, c) < d * f(nums[right], a, b, c):
                result.append(f(nums[left], a, b, c))
                left += 1
            else:
                result.append(f(nums[right], a, b, c))
                right -= 1
        return result[::d]

# 2/22/2018

class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        f = lambda x, a, b, c: a * x * x + b * x + c
        if a == 0:
            s = [f(num, a, b, c) for num in nums]
            if b >= 0:
                return s
            else:
                return s[::-1]

        x0 = -b / (2 * a)
        newnums = [(idx, abs(x - x0)) for idx, x in enumerate(nums)]
        newnums.sort(key=lambda x: x[1])

        s = [f(nums[idx[0]], a, b, c) for idx in newnums]
        return s if a > 0 else s[::-1]
