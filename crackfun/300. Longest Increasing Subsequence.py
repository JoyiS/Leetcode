'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

# Mehtod 1: O(n**2) DP the state is the length
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*(len(nums))
        maxlen = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    maxlen = max(maxlen, dp[i])
        return maxlen

# Method 2:  Binary Search
# The LIS array is used to keep track of the LIS
# res is the length of the LIS
# when a new element is seen, decide whether to put in into the LIS array by binary search to find the insertion index

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        LIS = [0]*len(nums)
        for x in nums:
            i = 0
            j = res
            while i!=j:
                mid = (i+j)//2
                if LIS[mid]>=x:
                    j=mid
                else:
                    i = mid+1
            LIS[i]=x
            if i==res:
                res+=1
        return res