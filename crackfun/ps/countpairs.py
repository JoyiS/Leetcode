class Solution():
    def countpairs(self, nums,D):
        pair = 0
        d = {}
        for x in nums:
            if x-D in d:
                pair+=1
            d[x] = 1
        return pair

    def sorted_search(self, nums, target):
        if not nums or len(nums)<1:
            return -1
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right+1)//2
            if nums[mid]> target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            return right
        return  -1