'''
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''


class Solution(object):
    def characterReplacement(self, s, k):
        count = [0] * 26
        n = len(s)
        end = 0
        res = 0

        def valid(start, end, k, count):
            return end - start + 1 - max(count) <= k

        for start in range(n):
            while end < n:
                t = ord(s[end]) - ord('A')
                count[t] += 1
                if valid(start, end, k, count):
                    res = max(res, end - start + 1)
                    end += 1
                else:
                    break
            if end < n:
                count[t] -= 1
            count[ord(s[start]) - ord('A')] -= 1
        return res

