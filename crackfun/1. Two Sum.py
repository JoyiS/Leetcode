'''
1/22/2018 Understand the hash function usage here
'''

class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i, n in enumerate(nums):
            if n in d:
                return (d[n], i)
            else:
                d[target-n]=i
        return (0,0)