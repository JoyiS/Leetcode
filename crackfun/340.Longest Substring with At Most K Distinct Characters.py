# Solution AC version
class Solution(object):
    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0 or not s:
            return 0

        maxlen = 0
        ss = ''
        d = {}
        cnt = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = i
                ss += s[i]
                maxlen = max(maxlen, len(ss))
            else:
                cnt += 1
                d[s[i]] = i
                ss += s[i]
                if cnt>k:
                    while ss and cnt > k:
                        if d[ss[0]] == start:
                            cnt -= 1
                            d.pop(ss[0])
                        ss = ss[1:]
                        start += 1
                maxlen = max(maxlen, len(ss))
        return maxlen


# TLE version
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0 or not s:
            return 0

        maxlen = 1
        for start in range(len(s)):
            end = start + maxlen
            d = {}
            cnt = 0
            flag = 0
            for i in s[start:end]:
                if i not in d:
                    d[i] = True
                    cnt += 1
                if cnt > k:
                    flag = 1
                    break
            while flag == 0 and end < len(s):
                if s[end] not in d:
                    d[s[end]] = True
                    cnt += 1
                if cnt > k:
                    flag = 1
                    break
                end += 1

            maxlen = max(end - start, maxlen)

        return maxlen
