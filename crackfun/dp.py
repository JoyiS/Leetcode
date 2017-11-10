#class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxpos = 0
        for i in range(0,len(nums)-1):
            if nums[i]+i>maxpos:
                maxpos = nums[i]+i
            if maxpos>=len(nums)-1:
                return True
            if nums[i]+i<nums[i+1]-1:
                return False
        if maxpos>=len(nums)-1:
            return True

        return False


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    d = [[0] * n] * m
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            d[0][j] = 0
            break
        else:
            d[0][j] = 1
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            d[i][0] = 0
            break
        else:
            d[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                d[i][j] = 0
            else:
                d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[m - 1][n - 1]


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid[0])
    m = len(grid)
    d = [[0 for i in range(n)] for j in range(m)]
    d[0][0] = grid[0][0]
    for i in range(1, m):
        d[i][0] = grid[i][0] + d[i - 1][0]
    for j in range(1, n):
        d[0][j] = grid[0][j] + d[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            d[i][j] = min(d[i - 1][j] + grid[i][j], d[i][j - 1] + grid[i][j])
    return d[m - 1][n - 1]


def numDecodings(s):
    if s == "" or s[0] == '0': return 0
    dp = [1, 1]
    for i in range(2, len(s) + 1):
        if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
            dp.append(dp[i - 1] + dp[i - 2])
        elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:
            dp.append(dp[i - 2])
        elif s[i - 1] != '0':
            dp.append(dp[i - 1])
        else:
            return 0
    return dp[len(s)]


def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    d = [[0 for i in range(j)] for j in range(1,n+1)]
    d[0][0] = triangle[0][0]

    for i in range(1, n):
        d[i][0] = d[i - 1][0] + triangle[i][0]
        d[i][i] = d[i-1][i-1] + triangle[i][i]
        for j in range(1, i):
            d[i][j] = min(d[i - 1][j] + triangle[i][j], d[i - 1][j - 1] + triangle[i][j])


    mind = min(d[n - 1][a] for a in range(n))
    return mind

#-----------------------FB questions--------------------------------

#125
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == '' or len(s) < 2:
        return True
    n = len(s)
    s = list(s)
    i = 0
    j = len(s) - 1

    def alphau(x):
        if (ord(x) <= ord('9') and ord(x) >= ord('0')) or (ord(x) <= 'Z' and ord(x) >= 'A') or (ord(x) <= 'z' and ord(x) >= 'a'):
            return True
        return False

    while i < j:
        while i < j and not alphau(s[i]):
            i += 1
        while i < j and not alphau(s[j]):
            j -= 1
        if i < j:
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        else:
            return True
    return True


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """

    d = ['1', '11']
    if n == 1:
        return d[0]
    if n == 2:
        return d[1]

    for i in range(2, n):
        count = 1
        last = d[i - 1][0]
        dnew = ''
        for j in d[i - 1][1:]:
            if j == last:
                count += 1
            else:
                dnew += str(count) + str(last)
                last = j
                count = 1

        d.append(dnew+str(count) + str(last))
    return d[-1]

def removeduplicate(nums):
    if not nums:
        return 0
    nums.sort()
    last = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] == last:
            nums = nums[:i] + nums[i + 1:]
        else:
            last = nums[i]
            i += 1
    return nums


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    vol = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    res = []
    while n > 0:
        res.append(vol[(n - 1) % 26])
        n = int((n-1)/26)
    return ''.join(res[::-1])


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    res = 1
    if n<0:
        x = 1/x
        n = -n

    while n:
        if n%2:
            res = res*x
            n = n-1
        res = res*res
        n = n/2
    return res

def meetingroom2(s):
    s.sort(key = lambda x:x[0])
    last = s[0][1]
    count = 1
    for i in s[1:]:
        if i[0]<last:
            count+=1
        last = i[1]
    return count


def wordBreak(s, wordDict):
    s1 = []
    s1.append(s)
    s2 = []
    flag = 1
    while flag:
        flag = 0
        for si in s1:
            for i in range(0, len(si)):
                if si[:i+1] in wordDict:
                   if i + 1 < len(si):
                      s2.append(si[i+1:])
                      flag = 1
                      print('NextTime')
                   else:
                       return True

        s1 = s2
        s2 = []
    return False