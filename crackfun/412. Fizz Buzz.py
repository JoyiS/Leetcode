class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list(range(1,n+1))
        res = [str(a) for a in res]
        res[3-1:len(res):3] = ['Fizz']*len(res[3-1:len(res):3])
        res[5-1:len(res):5] = ['Buzz']*len(res[5-1:len(res):5])
        res[15-1:len(res):15] = ['FizzBuzz']*len(res[15-1:len(res):15])
        return res