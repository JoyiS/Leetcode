class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        real_res = []
        for i in range(lower,upper+1):
            if i not in nums:
                res.append(i)
        last = res[0]
        lastend = last
        for i in range(1, len(res)):
            if res[i] == last + 1:
                last = res[i]
            else:
                if lastend!=last:
                    real_res.append(str(lastend)+'->'+str(res[i-1]))
                else:
                    real_res.append(str(lastend))
                lastend = res[i]
                last = res[i]
        # Adding the last one
        if last != lastend:
            real_res.append(str(lastend) + '->' + str(last))
        else:
            real_res.append(str(lastend))
        return real_res


#---------------------AC Solution
import itertools

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []

        lastNum = lower-1

        for num in itertools.chain( nums, [upper+1] ):
            if lastNum+2 == num:
                ret.append( str(lastNum+1) )
            elif lastNum+2 < num:
                ret.append( "{}->{}".format( lastNum+1, num-1 ) )

            lastNum = num

        return ret