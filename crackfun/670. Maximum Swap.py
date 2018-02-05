'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''

# First Time
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        strnum = list(str(num))
        strnum = [int(a) for a in strnum]

        for i in range(len(strnum)):
            if strnum[i + 1:]:
                lens = len(strnum[i + 1:])
                key = max(strnum[i + 1:])
                if strnum[i] < key:
                    strnum[i], strnum[i + 1 + (lens - 1 - strnum[i + 1:][::-1].index(key))] = strnum[i + 1 + (
                    lens - 1 - strnum[i + 1:][::-1].index(key))], strnum[i]
                    break
        return int(''.join(str(a) for a in strnum))

