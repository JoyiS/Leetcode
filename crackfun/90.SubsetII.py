class Solution(object):
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort() # remove repeated elements, the key is to sort!! this will make the work easier
        self.res = [[], [nums[0]]]
        self.num = [nums[0]]
        oldlen = len(self.res) - 1
        for i in nums[1:]:
            if i not in self.num:
                newsub = self.res + [x + [i] for x in self.res]
                self.num += [i]
            else:
                newsub = self.res + [x + [i] for x in self.res[oldlen:]]
            oldlen = len(self.res)
            self.res = newsub
        return self.res



