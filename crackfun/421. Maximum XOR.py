class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        for x in range(31, -1, -1):
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])
            tmp = ans | 1 << x
            for prefix in prefixSet:
                if tmp ^ prefix in prefixSet: # the num in nums still have difference at this bit
                    ans = tmp
                    break
        return ans

