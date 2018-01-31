class Solution(object):
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail

# Second time
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = None
        idx = 0
        for i in range(len(nums)):
            if nums[i] != last:
                last = nums[i]
                count = 1
                nums[idx] = nums[i]
                idx += 1
            else:
                count += 1
                if count >= 3:
                    continue
                nums[idx] = nums[i]
                idx += 1
        return idx


