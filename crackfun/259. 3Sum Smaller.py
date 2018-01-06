# This is a good two pointer problem!!
# The key to this problem is to reduce the time complexity
class Solution():
    def threeSumSmaller(self, nums, target):
        if len(nums)<3:
            return 0
        nums.sort()
        count = 0
        for i in range(0,len(nums)-2):
            j = i+1
            h = len(nums)-1
            while j<h:
                if nums[i]+nums[j]+nums[h]<target:
                    count += h-j
                    j += 1
                else:
                    h -= 1
        return count

