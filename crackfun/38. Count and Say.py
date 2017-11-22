class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = ['1', '11']
        if n == 1:
            return d[0]
        if n == 2:
            return d[1]

        for i in range(2, n):
            count = 1
            last = d[i - 1][0]
            dnew = ''
            for j in d[i - 1][1:]:
                if j == last:
                    count += 1
                else:
                    dnew += str(count) + str(last)
                    last = j
                    count = 1

            d.append(dnew+str(count) + str(last))
        return d[-1]