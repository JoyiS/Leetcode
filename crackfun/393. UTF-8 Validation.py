# Google high frequency: Bitwise operation.
# The solution is smart, clean.

def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
    return True

class Solution(object):
    def validUtf8(self, nums, start=0):
        while start < len(nums):
            first = nums[start]
            if   (first >> 3) == 0b11110 and check(nums, start, 3): start += 4
            elif (first >> 4) == 0b1110  and check(nums, start, 2): start += 3
            elif (first >> 5) == 0b110   and check(nums, start, 1): start += 2
            elif (first >> 7) == 0:                                 start += 1
            else:
                return False
        return True
# 2/18/2018
class Solution(object):
    def validUtf8(self, data, start=0):
        """
        :type data: List[int]
        :rtype: bool
        """

        def check(data, start, move):
            for i in range(start + 1, start + move + 1):
                if i >= len(data) or data[i] >> 6 != 0b10: return False
            return True

        while start < len(data):
            if data[start] >> 3 == 0b11110 and check(data, start, 3):
                start += 4
            elif data[start] >> 4 == 0b1110 and check(data, start, 2):
                start += 3
            elif data[start] >> 5 == 0b110 and check(data, start, 1):
                start += 2
            elif data[start] >> 7 == 0:
                start += 1
            else:
                return False
        return True

