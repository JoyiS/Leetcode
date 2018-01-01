# Method 1: Brute Force TLE

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        maxArea = heights[0]
        for i in range(0, len(heights)):
            j = i
            minh = heights[i]
            while j >= 0:
                maxArea = max(maxArea, minh * (i - j + 1))
                j -= 1
                minh = min(minh, heights[j])
        return maxArea

# Method 2: stack algorithm
def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
