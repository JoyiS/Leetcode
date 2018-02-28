'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''

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


# 2/28/2018
class Solution(object):
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
            print(bin(answer))
        return answer

'''
Build the answer bit by bit from left to right. Let’s say we already know the largest first seven bits we can create. How to find the largest first eight bits we can create? Well it’s that maximal seven-bits prefix followed by 0 or 1. Append 0 and then try to create the 1 one (i.e., answer ^ 1) from two eight-bits prefixes from nums. If we can, then change that 0 to 1.
'''
