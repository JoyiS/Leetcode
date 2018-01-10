'''
collection = empty
for sum_j in Sum:
    sum_i_count = how many sum_i in this collection that sum_j - upper <= sum_i <= sum_j - lower
    res += sum_i_count
    put sum_j into this collection
'''
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)

        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)

        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)  # BIT index starts from 1
            print(sum_j, BITree)
        return res


if __name__ == '__main__':
    nums = [-2,5,-1]
    lower = -2
    upper = 2
    a = Solution()
    a.countRangeSum(nums,lower,upper)