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


'''
TLE
'''


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        d = [10, 100, 1000, 10000, 100000, 1000000]
        m = n
        res = [1]
        while m > 1:
            if m / 10:
                res += [res[-1] * 10]
            m /= 10

        for i in range(2, n + 1):
            if i in d:
                continue
            strx = str(i)
            strxpre = strx[:-1]
            if not strxpre:
                res += [i]
                continue
            if len(str(int(strxpre) + 1)) == len(strxpre) and int(strxpre) // 10 == (int(strxpre) + 1) // 10:
                idx = res.index(int(strxpre) + 1)
                res = res[:idx] + [i] + res[idx:]
                continue
            if len(str(int(strxpre) + 1)) == len(strxpre) and int(strxpre) // 10 != (int(strxpre) + 1) // 10:
                key = str(int(strxpre) + 1)
                idx = res.index(int(key[0]))
                res = res[:idx] + [i] + res[idx:]
            else:
                res += [i]
        return res
