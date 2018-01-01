class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -target
        step = 1
        nextsum = 0
        while nextsum < target:
            nextsum += step
            step += 1
        step = step - 1
        if nextsum == target:
            return step
        n = nextsum - target
        if not n % 2:
            return step
        if n % 2:
            if not step % 2:
                return step + 1
            else:
                return step + 2



