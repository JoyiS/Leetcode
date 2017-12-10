class Solution(object):
    def combine(self, n, k):
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            rs=[]
            rs+=self.combine(n-1,k)
            part=self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs+=part
            return rs

# BackTracking
class Solution:
    # @return a list of lists of integers
    # 9:14
    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

# My solution TLE version
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        self.res = []
        self.k = k
        for i in range(0,len(nums)):
            self.dfs([nums[i]],nums[i+1:len(nums)])
        return self.res

    def dfs(self,ans,nums):
        if len(ans) == self.k:
            self.res+=[ans]
            return
        if not nums:
            return
        for i in range(len(nums)):
            self.dfs(ans+[nums[i]],nums[i+1:])
