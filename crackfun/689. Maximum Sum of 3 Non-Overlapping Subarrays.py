'''

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''

# My TLE Solution

class Solution(object):
    import operator
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}
        for i in range(len(nums) - k + 1):
            if i == 0:
                d[i] = sum(nums[i:i + k])
            else:
                d[i] = d[i - 1] + nums[i + k - 1] - nums[i - 1]

        sorted_d = sorted(d.items(), key = operator.itemgetter(1),reverse = True)
        self.res = -float('inf')
        for i in range(len(sorted_d)):
            idx, val = sorted_d[i]
            self.helper([idx], sorted_d[i+1:], val, k, nums)
        return self.bestidx

    def helper(self, residx, sorted_d, res, k, nums):
            if len(residx) == 2:
                for j in range(len(sorted_d)):
                    idxj, valj = sorted_d[j]
                    if all([abs(idxj - a) >= k for a in residx]):
                        res += valj
                        residx += [idxj]
                        break
                if len(residx) == 3 and res > self.res:
                    self.bestidx = sorted(residx)
                    self.res = res
                    #print(res)
                return
            if len(residx) == 1:
                for j in range(len(sorted_d)):
                    idxj, valj = sorted_d[j]
                    if abs(idxj - residx[0])>=k and ((min(residx[0],idxj)>=k or len(nums) - max(residx[0],idxj)>=2*k or abs(idxj-residx[0])>=2*k)):
                        self.helper(residx+[idxj], sorted_d[j+1:], res+valj, k, nums)


'''

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''


class Solution(object):
    import operator
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}
        for i in range(len(nums) - k + 1):
            if i == 0:
                d[i] = sum(nums[i:i + k])
            else:
                d[i] = d[i - 1] + nums[i + k - 1] - nums[i - 1]

        sorted_d = sorted(d.items(), key = operator.itemgetter(1),reverse = True)
        self.res = -float('inf')
        self.bestidx = [0,k,k*2]
        for i in range(len(sorted_d)-k):
            idx, val = sorted_d[i]
            self.helper([idx], sorted_d[i+1:], val, k, nums, i)
        return self.bestidx

    def helper(self, residx, sorted_d, res, k, nums,start):
            if len(residx) == 2:
                for j in range(start+1, len(sorted_d)):
                    idxj, valj = sorted_d[j]
                    if all([abs(idxj - a) >= k for a in residx]):
                        res += valj
                        residx += [idxj]
                        break
                if len(residx) == 3 and res > self.res:
                    self.bestidx = sorted(residx)
                    self.res = res
                    #print(res)
                return
            if len(residx) == 1:
                for j in range(start+1, len(sorted_d)-k):
                    idxj, valj = sorted_d[j]
                    if abs(idxj - residx[0])>=k and ((min(residx[0],idxj)>=k or len(nums) - max(residx[0],idxj)>=2*k or abs(idxj-residx[0])>=2*k)):
                        self.helper(residx+[idxj], sorted_d[j+1:], res+valj, k, nums, j)

# 1/28/2018
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        dpl = [(0, 0)] * (n)
        dpr = [(0, 0)] * (n)
        for i in range(k, n - 2 * k + 1):

            newsum = sum(nums[i - k:i])

            if i == k:
                dpl[i] = (i - k, newsum)
            else:
                if newsum > dpl[i - 1][1]:
                    dpl[i] = (i - k, newsum)
                else:
                    dpl[i] = (dpl[i - 1][0], dpl[i - 1][1])

        for i in range(n - 2 * k, k - 1, -1):
            newsum = sum(nums[i + k:i + 2 * k])
            if i == n - 2 * k:
                dpr[i] = (i + k, newsum)
            else:
                if newsum > dpr[i + 1][1]:
                    dpr[i] = (i + k, newsum)
                else:
                    dpr[i] = (dpr[i + 1][0], dpr[i + 1][1])

        res = -float('inf')

        for i in range(k, n - 2 * k + 1):
            newres = dpl[i][1] + dpr[i][1] + sum(nums[i:i + k])
            if newres > res:
                res = newres
                residx = [dpl[i][0], i, dpr[i][0]]

        return residx

#2/20/2018
'''
This is a good problem with 3 non-overlap arrays:
This kind of problem, focus on the middle one and use dp to keep record of the left and right arrays.
'''
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
