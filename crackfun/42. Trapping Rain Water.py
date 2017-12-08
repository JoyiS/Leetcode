# Method 1: Using Stack
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        stack = [0]
        water = 0
        for i in range(1, len(height)):
            if stack and height[i] > height[stack[-1]]:
                bottom = stack[-1]
                stack.pop()
                while stack and height[stack[-1]] < height[i]:
                    water += (i - stack[-1] - 1) * (height[stack[-1]] - height[bottom])
                    bottom = stack[-1]
                    stack.pop()
                if stack:
                    water += (i - stack[-1] - 1) * (height[i] - height[bottom])
            stack.append(i)
        return water

# Method 2: Two pointers
class Solution(object):
    def trap(self, height):
        n=len(height)
        l,r,water,minHeight = 0,n-1,0,0
        while l<r:
            while l<r and height[l]<=minHeight:
                water+=minHeight - height[l]
                l+=1
            while r>l and height[r]<=minHeight:
                water+=minHeight - height[r]
                r-=1
            minHeight = min(height[l],height[r])
        return water