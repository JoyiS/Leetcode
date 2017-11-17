# Method 1: The tricky part of this problem is whether to set nums[i] = nums[i-1] to make change at the current position
# or to modify nums[i-1] to nums[i] to change the previous one.
# Examples:
# 1936: when iterates to '3', need to modify nums[i-1] to nums[i]
# 1991: when iterates to '1', need to modify num[i] to nums[i-1]

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
                if i==1 or nums[i-2]<=nums[i]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                if count>1:
                    return False
        return True

# Method 2: not keep a sorted nums
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chance = 1
        for x in range(len(nums)):
            if x and nums[x] < nums[x - 1]:
                #if not chance:
                #     return False
                chance -= 1
                if x > 1 and nums[x] <= nums[x - 2]:
                    nums[x] = nums[x - 1]
        return True

