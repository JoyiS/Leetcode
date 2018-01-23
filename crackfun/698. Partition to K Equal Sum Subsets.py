'''
This is a good problem for DFS.
(1) One key is to sort reversly. This is very important 0 < nums[i] < 10000.!!!
(2) DFS idea, need the following inputs:
k: to represent the number of divide subarrays
cum: current sum
index: to avoid time waste, start from the next index

'''

'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if k==1: return True

        self.n=len(nums)
        if k>self.n: return False

        total=sum(nums)
        if total%k: return False

        self.target=total/k
        visit=[0]*self.n

        nums.sort(reverse=True)
        def dfs(k,ind,sum):
            if k==1: return True
            if sum==self.target:
                return dfs(k-1,0,0)
            for i in range(ind,self.n):
                if not visit[i] and sum+nums[i]<=self.target:
                    visit[i]=1
                    if dfs(k,i+1,sum+nums[i]):
                        return True
                    visit[i]=0
            return False

        return dfs(k,0,0)