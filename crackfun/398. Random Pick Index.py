class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        y = -1
        for i, num in enumerate(self.nums):
            if num == target:
                x = random.random()
                if x > y:
                    y = x
                    res = i
        return res


# Method 2: Be straightforward

class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)