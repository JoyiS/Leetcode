'''
The idea:
1. divide the problem into horizontal direction and vertical direction (row and column)
2. for colomn : use two pointer to sweep from left to right: fix left, sweep right to the end for inner loop and then left+1
3. for the column, need to search the dynamic range for optimal solution. Use binary tree for fast search!
'''
import bisect
class Solution(object):
    def maxSubArraylessK(self, nums, k):
        """
        we need to find the sum[right]-sum[left]<=k
        since the bitsect return the index of the sorted value
        we can't directly pop the nums[idx]
        we should use insort from the bisect
        """
        # python set() doesn't support indexing, using list instead
        # similar as the c++ or java set()

        cumset = []
        cumset.append(0)
        maxsum = -1 << 32
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            # find the lower bound of the index
            # This is the row idx here
            idx = bisect.bisect_left(cumset, cursum - k)
            if 0 <= idx < len(cumset):
                maxsum = max(maxsum, cursum - cumset[idx])
            # using insort instead of append since bisect_left reason
            bisect.insort(cumset, cursum)
        return maxsum

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        The python solution hasn't a good time performance,
        since lack some of the datatype to do
        I am trying to imitate the way solved in c++ or Java
        The related quesiton might be:
        1. #53. Maximum Subarray
        2. Maximum Subarray sum less or equal than K
        3. maximun sum of rectangle
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        res = -(1 << 32)
        # using two pointer to record the scan position
        for left in range(col):
            # reset mem to store the row data
            cursums = [0 for _ in range(row)]
            # since the rectange has area>0
            right = left
            while right < col:
                # count one row
                for i in range(row):
                    cursums[i] += matrix[i][right]
                # find the max in this row
                curarrmax = self.maxSubArraylessK(cursums, k)
                res = max(res, curarrmax)
                right += 1

        return res