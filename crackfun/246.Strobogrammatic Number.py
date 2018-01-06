class Solution:
    # @param {string} num
    # @return {boolean}
    # 回文数
    def isStrobogrammatic(self, num):
        dic = {'9': '6', '6': '9', '1': '1', '8': '8', '0': '0'}

        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in dic or dic[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

# 1/5/2018 second time this problem
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        snum = str(num)
        i = 0
        j = len(snum) - 1
        while i <= j:
            if (snum[i] not in dict) or (snum[j] not in dict) or (dict[snum[i]] != snum[j]):
                return False
            i += 1
            j -= 1
        return True
