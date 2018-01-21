'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

# method 1: Binary Search
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            if self.helper(nums, mid, m):
                high = mid
            else:
                low = mid + 1
        return low

    def helper(self, nums, mid, m):
        cnt = 1
        ressum = 0
        for i in range(len(nums)):
            ressum += nums[i]
            if ressum > mid:
                ressum = nums[i]
                cnt += 1
                if cnt > m: return False
        return True


# Method 2: Dp tbd