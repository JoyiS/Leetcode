class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        mina = target
        minmaxa = 'z'
        flag = 0
        for a in letters:
            if ord(target)<ord(a)<=ord(minmaxa):
                flag = 1
                minmaxa = a
            elif ord(a)<ord(mina)<=ord(target):
                mina = a
        return minmaxa if flag==1 else mina