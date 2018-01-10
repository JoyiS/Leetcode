# New method, use cache, better than back tracking time complexity/...
# dfs with a dictionary to avoid repeating computations....

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = dict()
        def solve(idx, nums):
            if not nums: return 1
            key = idx, tuple(nums)
            if key in cache: return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i+1:])
            cache[key] = ans
            return ans
        return solve(1, range(1, N + 1))


# ------- TLE solution
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.res = 0
        self.dfs([], {}, N)
        return self.res

    def dfs(self, array, d, N):
        if len(array) == N:
            self.res += 1
            return
        i = len(array) + 1
        for x in range(1, N + 1):
            if x not in d and (not x % i or not i % x):
                array += [x]
                d[x] = 1
                self.dfs(array, d, N)
                d.pop(x)
                array.pop()
        else:
            return

