# AC solution
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        result = []
        nums.append(upper + 1)
        pre = lower - 1
        for i in nums:
            if (i == pre + 2):
                result.append(str(i - 1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i
        return result

# ------------- This solution gives memory limit!!
# for exmaple nums = [0] lower  = 0 upper = 2**31-1
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
        for i in range(lower,upper+1): # This increase the time/space complexity a lot! which is bad
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