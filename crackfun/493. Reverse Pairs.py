# Great question : Reverse pairs
# link: https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs


class Solution(object):
    def reversePairs(self, nums):
        if not nums:
            return 0

        def count(start, end):
            if start >= end:
                return 0
            mid = (end + start) / 2
            total_count = count(start, mid) + count(mid + 1, end)
            i, j = start, mid + 1
            while i <= mid:
                while j <= end and nums[i] > nums[j] * 2:
                    j += 1
                total_count += j - (mid + 1)
                i += 1
            nums[start: end + 1] = sorted(nums[start: end + 1])  # This is important as well.
            return total_count

        return count(0, len(nums) - 1)