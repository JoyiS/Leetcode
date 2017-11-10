# Problem 697

def degree(nums):
    # use dictionary to store data
    # use max/min to record the smallest and largest index of the data
    # use cnt to count the frequency of the data
    dictnum = {}

    for idx,num in enumerate(nums):
        if num not in dictnum:
            cnt=1
            minidx=idx
            maxidx=idx
            dictnum[num] = [cnt,minidx,maxidx]
        else:
            cnt = dictnum[num][0]+1
            minidx = dictnum[num][1]
            maxidx = idx
            dictnum[num] = [cnt,minidx,maxidx]
    deg = max(dictnum[a][0] for a in nums)
    deg_nums = [a for a in dictnum.keys() if dictnum[a][0] == deg]
    minlength = min(dictnum[a][2]-dictnum[a][1] + 1 for a in deg_nums)
    return dictnum, deg, minlength


# 696 count sub string
# recursive  # What I have got is wrong (00110)
def countsubstr(s):
    if s is None:
        return None
    # t = 0
    # for i in range(len(s)):
    #     ss = s[:i+1]
    #     if rule(ss):
    #         backpos = i
    #         for j in range(1,len(ss)):
    #             if j+1<len(ss) and int(ss[j])^int(ss[j+1]) ==1:
    #                 backpos = j
    #         print('string till  ' + str(i) +' : ' + ss +' backpos  ' + str(backpos))
    #         t = t+1+countsubstr(s[backpos:])
    size = len(s)
    cnt = [0, 0]
    last = None
    ans = 0
    for c in s:
        c = int(c)
        if c != last:
            cnt[c] = 0
        cnt[c] += 1
        if cnt[c] <= cnt[1 - c]:
            print(str(c) + ' string is ' + str(cnt))
            ans += 1
        last = c

    return ans

def cntsubstr(s):
    cnt=[0,0]
    res = 0
    Last = None
    for c in s:
        c = int(c)
        if c != Last:
            cnt[c]=0
        cnt[c]+=1
        if cnt[c]<=cnt[1-c]:
            res=res+1
    return res


def rule(s):
    if s is not None:
        count0 = 0
        count1 = 0
        flag = 0
        prev = int(s[0])
        for i in s:
            flag+=int(i)^int(prev)
            if i =='0':
                count0 += 1
            if i =='1':
                count1 += 1
            prev = i
        if count0 == count1 and flag==1:
            return True
    return False


# 388 Longest file path
def longestfilepath(input):
    newrow ='\n'
    newtab = '\t'
    fileid = '.'
    level = []
    lena = []
    res = 0
    k = 0
    for s in input.split(newrow):
        levelnew, lenanew = countss(s, newtab)
        level.append(levelnew)
        lena.append(lenanew)
        if fileid in s:
            j=k-1
            lenall = lenanew
            currentlevel = levelnew
            print(s + ' : current level : ' + str(currentlevel) + ' , value j :' + str(j))
            while j>=0 and currentlevel>=0:
                if level[j] < currentlevel:
                    lenall += lena[j]+1
                    print('currentl level: ' + str(currentlevel) +', add str:' + str(j)+input.split(newrow)[j])
                    currentlevel = currentlevel - 1
                j-=1
            res = max(lenall,res)
        k = k + 1
    return res




def countss(s,ss):
    count = 0
    lena = len(s)
    if ss in s:
        snew = s.split(ss)
        for a in snew:
            if a=='':
                count = count+1
            else:
                lena = len(a)
    return count, lena


# 695
# Method 1: using explored to store the explored nodes: this method will exceed the time limit when input is large
class Solution(object):
    def maxArea(self, grid):
        def bfs(grid, x, y):
            explored = []
            queue = []
            if grid[x][y]:
                queue.append([x, y])

                while queue:
                    [nodex, nodey] = queue.pop(0)
                    if [nodex, nodey] not in explored:
                        explored.append([nodex,nodey])
                        dx = [1, 0, -1, 0]
                        dy = [0, 1, 0, -1]
                        for dxx, dyy in zip(dx, dy):
                            if nodex + dxx >= 0 and nodex + dxx < len(grid) and nodey + dyy >= 0 and nodey + dyy < len(grid[0]):
                                if [nodex + dxx, nodey + dyy] not in explored and grid[nodex + dxx][nodey + dyy] == 1:
                                    queue.append([nodex + dxx, nodey + dyy])
            return len(explored)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == 1:
                    res = max(res, bfs(grid, x, y))
        return res

# Method 2:
# Not using explored, but to turn that point into 0
# use a counter to add one whenever pop(0)

# 693
def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    n = bin(n)
    return all(n[x] != n[x + 1] for x in range(len(n) - 1))


def hasAlternatingBits( n):
    """
    :type n: int
    :rtype: bool
    """
    last = n & 1
    n = n >> 1
    while n > 0:
        bit = n & 1
        if bit == last:
            return False
            break
        last = bit
        n = n >> 1
    return True


# 346
class movingAve(object):
    def __init__(self,sizelim):
        self.sizelim = sizelim
        self.item = []
    def insert(self,d):
        self.item.append(d)
    def remove(self):
        self.item.pop(0)
    def size(self):
        return len(self.item)
    def next(self,d):
        if self.size()<self.sizelim:
            self.insert(d)
            return sum(self.item)/self.size()
        else:
            self.remove()
            self.insert(d)
            return sum(self.item)/self.size()

#288 Unique word abberavation
def unique(s,word):
    def wordabbr(s):
        d={}
        for ss in s:
            ssabb = ss
            if len(ss)>2:
                ssabb = ss[0]+str(len(ss)-2)+ss[-1]
            if ssabb not in d:
                d[ssabb] = []
                d[ssabb].append(ss)
            elif ss!=d[ssabb][0]:
                d[ssabb]=['']
            else:
                pass
        return d

    if len(word) > 2:
        wordnew = word[0] + str(len(word) - 2) + word[-1]
    else:
        wordnew = word
    dd = wordabbr(s)
    if wordnew not in dd or (wordnew in dd and dd[wordnew][0]==word):
        return True
    return False

#
def isStrobo(num):
    def mapdig(dig):
        digin = [0,1,6,8,9]
        digout = [0,1,9,8,6]
        if dig in digin:
            return digout[digin.index(dig)]
        else:
            return None

    s = str(num)
    i = 0
    j = len(s)-1
    while i<=j:
        if mapdig(int(s[i])) is not None and mapdig(int(s[i])) == int(s[j]):
            i=i+1
            j=j-1
        else:
            return False
    return True

    def reverseVowels( s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        i=0
        j=len(s)-1
        while i<=len(s)-1 and i < j:
            while s[i] not in vowels:
                i+=1
            while s[j] not in vowels:
                j-=1
            if i<j:
                temp = s[j]
                tempi = s[i]
                if j==len(s)-1:
                    s = s[:i] + temp + s[i + 1:j] + tempi
                else:
                    s = s[:i]+temp+s[i+1:j]+tempi+s[j+1:]
            else:
                break
            i+=1
            j-=1
            print(str(i) +',' +str(j))
        return s


class Logger(object):
    def __init__(self,dlog,slog):
        self.dlog = []
        self.slog = []
    def shouldPrintMessage(self,d,s):
        if s not in self.slog:
            self.dlog.append(d)
            self.slog.append(s)
            return True
        else:
            if d - self.dlog[(len(self.slog)-1 - self.slog[::-1].index(s))] < 10:
                return False
            else:
                self.dlog.append(d)
                self.slog.append(s)
                return True


# Memory Limit Exceeds
def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    a = 1
    b = 9
    step = [a * b]
    number = [a*b]
    while sum(step) < 2**31:
        a = a + 1
        b = b * 10
        step.append(a * b)
        number.append(number[-1]*10+9)

    idx, end = next(x for x in enumerate(step) if x[1] >= n)
    if idx > 0:
        nidx = int((n-sum(step[:idx])-1)/(idx+1))
        s = number[idx-1]+1+nidx
        didx = (n-sum(step[:idx])-1)%(idx+1)
        return int(str(s)[didx])
    return int(n)

def paintFence(n,k):
    if n==0:
        return 0
    if n==1:
        return k
    if n==2:
        return k+k*(k-1)
    samecount = k;
    diffcount = k * (k - 1);
    for i in range(3,n):
        temp = diffcount
        diffcount = (samecount*(k-1) + diffcount*(k-1))
        samecount = temp
    return samecount+diffcount


def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s = sorted(s)
    t = sorted(t)
    i = 0
    while i<len(s):
        if s[i]!=t[i]:
            return s[t]
        i=i+1
    return t[-1]


def readBinaryWatch(n):
    """
    :type num: int
    :rtype: List[str]
    """
    hstr = [8, 4, 2, 1]
    mstr = [32, 16, 8, 4, 2, 1]
    hlimit = 11
    mlimit = 59
    timeres = []
    import itertools
    def timestr(n, string, maxlimit):
        res = []
        if n == 0:
            return [0]
        if n >= 1:
            for x in itertools.combinations(string, n):
                if sum(list(x)) <= maxlimit:
                    res.append(sum(list(x)))
            if res == []:
                return [-1]
        return res
    for i in range(0, n+1):
        hourstr = timestr(i, hstr, hlimit)
        minstr = timestr(n-i, mstr, mlimit)
        for hh in hourstr:
            for mm in minstr:
                if hh>=0 and mm>=0:
                    hh = str(hh)
                    if mm <= 9:
                        mm = '0' + str(mm)
                    else:
                        mm = str(mm)
                    timehm = hh + ':' + mm
                    timeres.append(timehm)

    return timeres


#293
def flipgame(s):
    if s==None:
        return []
    if len(s)<2:
        return []
    last = s[0]
    cstr = ['-','+']
    res = []
    for i in range(1,len(s)):
        idx = cstr.index(s[i])
        if cstr[idx] == last:
            res.append(s[:i-1]+cstr[1-idx]*2+s[i+1:])
        last = s[i]
    return res


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    dxx = [1, 0, -1, 0]
    dyy = [0, 1, 0, -1]

    def bfs(grid, x, y):
        count = 0
        explored = []
        if grid[x][y]:
            queue = [[x, y]]
            count += (x == 0) + (x == len(grid) - 1) + (y == 0) + (y == len(grid[0]) - 1)
            while queue:
                point = queue.pop(0)
                if point not in explored:
                    explored.append(point)
                    px = point[0]
                    py = point[1]
                    print('[x,y]: '+ str(px)+','+str(py) + ': count: ',str(count))
                for dx, dy in zip(dxx, dyy):
                    if [px + dx, py + dy] not in explored and [px + dx, py + dy] not in queue:
                        if px + dx < len(grid) and py + dy < len(grid[0]) and px + dx >= 0 and py + dy >= 0:
                            if grid[px + dx][py + dy]:
                                count += (px + dx == 0) + (px + dx == len(grid) - 1) + (py + dy == 0) + (py + dy == len(grid[0]) - 1)
                                queue.append([px + dx, py + dy])
                                print('adding to queue [x,y]: ' + str(px+dx) + ',' + str(py+dy) + ': count: ', str(count))
                                print(explored)
                            else:
                                count += 1
        return count

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j]:
                res = max(res, bfs(grid, i, j)[0])
                break
    return res

def groupshiftstr(s):
    d=[]
    lend = []
    def compc(c1,c2):
        if len(c1)!=len(c2):
            return False
        if c1==None:
            return True
        dd = ord(c1[0])-ord(c2[0])
        for i,j in zip(c1,c2):
            t=ord(i)-ord(j)
            if t<0:
                t = t+26
            if t != dd:
                return False
        return True
    for c in s:
        if len(c) in lend and compc(c,d[lend.index(len(c))][0]):
            d[lend.index(len(c))].append(c)
        else:
            d.append([c])
            lend.append(len(c))
    return d


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item = []
        self.trackMin = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.item.append(x)
        if self.trackMin == None:
            self.trackMin.append(x)
        else:
            if x < min(self.trackMin):
                self.trackMin.append(x)
            else:
                self.trackMin.append(min(self.trackMin))

    def pop(self):
        """
        :rtype: void
        """
        if self.item:
            return self.item.pop()
            self.trackMin = self.trackMin[:-1]
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.item:
            return self.item[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.trackMin:
            return self.trackMin[-1]
        else:
            return None


if __name__ == "__main__":
    nums = [1,2,2,3,1]
    dictnum,deg,minlength = degree(nums)


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """

    n=bin(n)[2:]
    while len(n) > 1:
        if n[-1] == '0':
            n=n[:-1]
        else:
            return False
    if n == '1':
        return True
    return False

def wordsquare(s):
    for j in range(len(s)):
        a = ''
        for i in range(len(s)):
            if j<len(s[i]):
                a=a+(s[i][j])
        if s[j] != a:
            return False
            break
    return True


def validWordAbbreviation(s1,s2):
    digit = '0123456789'
    i=j=0
    while i < len(s1) and j < len(s2):
        if s1[i]==s2[j]:
            print(s1[i],s2[j])
            i+=1
            j+=1
        else:
            print(s1[i], s2[j])
            t = s2[j]
            if t in digit:
                num = 0
                while j<len(s2) and t in digit:
                    num = num*10+int(t)
                    j+=1
                    t=s2[j]
                i = i+num
                print(i)
            else:
                return False
    return True


def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """

    while n / 3 >= 1:
        n = n / 3
        if n != int(n):
            return False
            break
    if n == 1:
        return True
    return False


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        res = 0
        for point in points:
            ppp = {}
            for pp in points:
                ppx = ((point[0] - pp[0]) ** 2)
                ppy = ((point[1] - pp[1]) ** 2)
                if ppx + ppy not in ppp:
                    ppp[ppx + ppy] = [pp]
                else:
                    ppp[ppx + ppy].append(pp)
            for key in ppp.keys():
                if len(ppp[key]) >= 2:
                    res += len(ppp[key]) * (len(ppp[key]) - 1)

        return res


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    i=0
    while i<=len(nums)-1:
        temp = nums[i]
        if temp != i + 1:
            nums[i] = nums[temp- 1]
            nums[temp - 1] = temp
            temp = nums[i]
            print(nums)
        else:
            i=i+1
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i in range(0, len(nums)):
        while (nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]):
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
            print(nums)
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res


def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) < 2:
        return False
    if s == s[0]*len(s):
        return True
    mid = int(len(s) / 2)
    i = 0
    j = mid
    while i < j and j < len(s) and mid >= 1:
        if s[i] == s[j]:
            i += 1
            j += 1
            if i == mid:
                break
        else:
            i = 0
            j = mid - 1
            mid = mid - 1
    if mid > 0:
        substr = s[:mid]
        n = len(s) / len(substr)
        if substr * n == s:
            return True
    return False


def findRadius(houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    d = []
    houses = sorted(houses)
    heaters = sorted(heaters)
    for i in houses:

        if i in heaters:
            d.append(0)
        else:
            nexti = [(idx, a) for idx, a in enumerate(heaters) if a > i]
            if nexti:
                nextidx = nexti[0][0]
                if nextidx >= 1:
                    beforeidx = nextidx - 1
                    d.append(max(heaters[nextidx] - i, i - heaters[beforeidx]))
                else:
                    d.append(nexti[0][1] - i)
            else:
                beforei = [(idx, a) for idx,a in enumerate(heaters) if a < i]
                beforeidx = beforei[-1][0]
                d.append(i - heaters[beforeidx])
    return max(d)

name = ['Joy','SC','David','April','Charbel','Vara']
a= [11,11+18/4,13+18/4,14,12+18/2,12]
sum(a)
b = [aa*1.09*1.18 for aa in a]
sum(b)


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums is None:
        return [[]]
    d = [[]]

    for i in nums:
        dtemp = [d0+[i] for d0 in d]
        d += dtemp
    return d


#161 One edit distance
def oneeditdis(s,t):
    if abs(len(s) - len(t)) > 1:
        return False
    if abs(len(s)-len(t)) == 1:
        i = 0
        count = 0
        while s and t:
            while i<len(s) and i<len(t) and s[i]==t[i]:
                i+=1
            if i==len(s) or i==len(t):
                return True
            if len(s)>=len(t):
                s = s[:i]+s[i+1:]
            else:
                t = t[:i]+t[i+1:]
            count+=1
        return True
    if len(s)==len(t):
        count =0
        for i in range(len(s)):
            if s[i]!=t[i]:
                count+=1
            if count>1:
                return False
        return True


