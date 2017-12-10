class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        if target == nums[l] or target == nums[r]:
            return True
        if nums[l] == nums[r]:
            pivot = nums[l]
            while nums and nums[0] == pivot:
                nums.pop(0)
            while nums and nums[-1] == pivot:
                nums.pop()

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

