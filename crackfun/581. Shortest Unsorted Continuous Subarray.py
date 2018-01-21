'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


'''
这道题目两种方法：
1） 排序，O（nlogn) , space(O(n))
2)  visulization 之后，巧妙的小方法， 遍历就好。 O（n) space O(1)


'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        numscopy = nums
        nums = sorted(nums)
        if numscopy == nums:
            return 0
        start = 0
        end = len(nums) - 1
        for i in range(len(nums)):
            if numscopy[i] != nums[i]:
                start = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if numscopy[i] != nums[i]:
                end = i
                break
        return end - start + 1


# Method 2

class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) < 2:
            return 0
        flag = 0
        flag1 = 0
        minval = float('inf')
        maxval = -float('inf')
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = 1
            if flag:
                minval = min(minval, nums[i])

        for j in range(len(nums) - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                flag1 = 1
            if flag1:
                maxval = max(maxval, nums[j])
        if minval == float('inf') and maxval == -float('inf'):
            return 0

        start = 0
        end = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] > minval:
                start = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] < maxval:
                end = j
                break
        return end - start + 1 if end - start >= 0 else 0