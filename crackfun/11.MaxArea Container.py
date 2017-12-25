class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maxArea_value = 0
        xLen = len(height)
        left = 0
        right = xLen-1
        while (left!=right):
            if height[left]<=height[right]:
                maxArea_value = max(height[left]*(right-left),maxArea_value)
                left = left + 1
            else:
                maxArea_value = max(height[right]*(right-left),maxArea_value)
                right = right - 1
        return maxArea_value