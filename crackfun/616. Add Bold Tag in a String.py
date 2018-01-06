'''
Given a string s and a list of strings dict,
you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap,
you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
    Input:
    s = "abcxyz123"
    dict = ["abc","123"]
    Output:
    "<b>abc</b>xyz<b>123</b>"
Example 2:
    Input:
    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    Output:
    "<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
'''


# Very Proud of myself
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        # Find words
        start = []
        for d in dict:
            for i in range(len(s)):
                if d in s[i:]:
                    stt = s.find(d, i)
                    start.append([stt, stt + len(d)])

        if not start:
            return s
        start.sort(key=lambda x: x[0]) # This is a key line to sort the indexes

        # Merge words
        resstart = []
        resend = []
        lastend = -1
        for i in range(len(start)):
            if start[i][0] > lastend:
                resstart += [start[i][0]]
                if lastend != -1:
                    resend += [lastend]
            lastend = max(lastend,start[i][1])  # This is a key line (take the max)
        resend += [lastend]

        # Generate Output
        news = ''
        for k, z in zip(range(len(resstart)), range(len(resend))):
            if k < len(resstart)-1:
                news += '<b>' + s[resstart[k]:resend[z]] + '</b>' + s[resend[z]:resstart[k + 1]]
            else:
                news += '<b>' + s[resstart[k]:resend[z]] + '</b>' + s[resend[z]:]

        news = s[:resstart[0]] + news
        return news
