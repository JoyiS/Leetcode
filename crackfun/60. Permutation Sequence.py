class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        res = ''
        k-=1
        nums = list(range(1,n+1))
        while n>0:
            n-=1
            index, k = divmod(k, math.factorial(n))
            res+=str(nums[index])
            nums.remove(nums[index])
        return res