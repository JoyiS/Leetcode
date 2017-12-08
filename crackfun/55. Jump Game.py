class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        if len(nums)==1:
            return True
        i=0
        while i<=(len(nums)-1) and i<=maxpos:
            if nums[i]+i>maxpos:
                maxpos=nums[i]+i
            if maxpos>=len(nums)-1:
                return True
            i+=1
        return False