class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        if digits[-1] < 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            newdigits = []
            carry = 1
            for i in digits[::-1]:
                newdigits.append((i+carry)%10)
                carry = (i+carry)/10
            if carry>0:
                newdigits.append(carry)
            return newdigits[::-1]