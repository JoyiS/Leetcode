# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if guess(mid) == -1:
                high = mid - 1
                continue
            if guess(mid) == 1:
                low = mid + 1
                continue
            if guess(mid) == 0:
                return mid
