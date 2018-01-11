class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nl = str(n)
        lenn = len(nl)
        targetIndex = 0
        changeIndex = 0
        for i in range(lenn - 1, 0, -1):
            if nl[i] > nl[i - 1]:
                targetIndex = i - 1
                break
        for i in range(lenn - 1, -1, -1):
            if nl[i] > nl[targetIndex]:
                changeIndex = i
                break
        temp1 = nl[targetIndex]
        temp2 = nl[changeIndex]
        nl = nl[:targetIndex] + temp2 + nl[targetIndex + 1:]
        nl = nl[:changeIndex] + temp1 + nl[changeIndex + 1:]

        if changeIndex == targetIndex == 0:
            return -1
        else:
            nl = nl[:targetIndex + 1] + nl[targetIndex + 1:][::-1]
            n = int(nl)
            if n > 2 ** 31 - 1:  # 
                return -1
        return n

