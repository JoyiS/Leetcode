'''
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:
Input: [1,2,4,-1,2], 2
Output: [1,3,5]
Example 2:
Input: [1,2,4,-1,2], 1
Output: []
Note:
Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].

'''

# My Solution (Paritially correct has issue with lexicographically smallest such path)
class Solution:
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[-1] == -1:
            return []
        if not B:
            return len(A) == 1 and A != -1
        dp = [(float('inf'), [i + 1]) for i in range(len(A))]
        dp[0] = (A[0], [1])
        for i in range(1, len(A)):
            if A[i] != -1:
                for j in range(max(0, i - B), i):
                    if dp[j][0] + A[i] < dp[i][0] or (
                                dp[j][0] + A[i] == dp[i][0] and str(dp[j][1][-1]) < str(dp[i][1][-1])):
                        dp[i] = (dp[j][0] + A[i], dp[j][1] + [i + 1])

        return dp[-1][1] if dp[-1][0] != float('inf') else []

# Solution
# This Solution is very good.
'''
对于这种lexicographically排序的题目，利用list的排序性质，简直写的优秀好吗
'''
class Solution:
    def cheapestJump(self, A, B):
        if not A or A[0] == -1: return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1: continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
            print(dp[j])
        return dp[-1][1:] if dp[-1][0] < float('inf') else []