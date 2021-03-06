'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        newS = []
        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z': newS.append(i)
            elif 'A' <= i <= 'Z': newS.append(chr(ord(i) - ord('A') + ord('a')))
        return newS == newS[::-1]