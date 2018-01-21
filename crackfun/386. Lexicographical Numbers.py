class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = []
        x = 1
        while x <= n:
            stack.append(x)
            result.append(x)
            x *= 10
        while stack:
            y = stack.pop()
            if y % 10 == 9: continue
            y += 1
            while y <= n:
                stack.append(y)
                result.append(y)
                y *= 10
        return result


