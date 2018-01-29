# Method 1: Brute Force
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {}
        d['1'] = []
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        if len(digits)<1:
            return []
        res = d[digits[0]]
        if len(digits) == 1 :
            return res
        for i in digits[1:]:
            newres = [resj + inewk for resj in res for inewk in d[i]]
            res = newres
        return res

# METHOD 2: BACKTRACKING(回溯发)
# return all possible combinations(all results) : use backtracking

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        # global variable
        d = {}
        d['1'] = []
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']

        self.res = []

        def dfs(digits, index, temp, d):
            if len(temp) == len(digits):
                self.res.append("".join(x for x in temp))
                return

            for char in d[digits[index]]:
                temp.append(char)
                dfs(digits, index + 1, temp, d)
                temp.pop()  # This is important!!!!

        dfs(digits, 0, [], d)
        return self.res


# second time 1/26/2018
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = []
        self.helper(digits, '')
        return self.res

    def helper(self, digiIn, temp):
        if digiIn == '':
            if temp != '':
                self.res += [temp]
            return
        for x in self.d[digiIn[0]]:
            self.helper(digiIn[1:], temp + x)
