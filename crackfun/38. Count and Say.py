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

# 2/15/2018
class Solution:
    def countAndSay(self, n):

        if n == 1:
            return '1'
        stri = '1'
        for i in range(2,n+1):
            last = stri[0]
            newstr = ''
            cnt = 1
            for j in range(1,len(stri)):
                if stri[j]==last:
                    cnt+=1
                else:
                    newstr+=str(cnt)+last
                    cnt = 1
                    last = stri[j]
            stri = newstr + str(cnt)+last
        return stri