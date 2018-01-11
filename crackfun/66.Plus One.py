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

# Second Time not using array method.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        p = -1
        i = 0
        flag = 0
        while i < len(digits):
            if digits[i] != 9:
                p += 1
                i += 1
            if digits[i] == 9:
                while i < len(digits) and digits[i] == 9:
                    i += 1
                if i < len(digits)-1 and digits[i]!=9:
                    flag = 1
                    p = i
        if flag==1:
            p -= 1

        if p == -1:
            return [1] + [0] * len(digits)
        else:
            digits[p] += 1
            p += 1
            while p < len(digits):
                digits[p] = 0
                p+=1
            return digits