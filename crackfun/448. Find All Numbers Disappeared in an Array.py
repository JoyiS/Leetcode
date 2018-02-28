'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):

        return list(set(range(1, len(nums)+1)) - set(nums))

# Method 2:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                res += [i + 1]
        return res

#Method 3:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        i=0
        while i<len(nums):
            idx = nums[i]-1
            if nums[i]!=nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
                i-=1
            i+=1
       #print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res+=[i+1]
        return res