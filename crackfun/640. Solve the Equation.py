class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        NoSol = 'No solution'
        InfiSol = 'Infinite solutions'
        OneSol = 'x='

        lastisop = True
        signchange = 1
        digistack = []
        xstack = []
        idx = len(equation)
        ii = 0
        while ii < len(equation):
            i = equation[ii]
            if i == 'x':
                if lastisop or not digistack:
                    xstack += [signchange]
                else:
                    xstack += [digistack.pop()]

            lastisop = False
            if i == '+':
                lastisop = True
                if ii < idx:
                    signchange = 1
                else:
                    signchange = -1
            if i == '-':
                lastisop = True
                if ii < idx:
                    signchange = -1
                else:
                    signchange = 1
            if i == '=':
                lastisop = True
                signchange = -1
                idx = ii
            if i.isdigit():
                lastisop = False
                num = 0
                while ii < len(equation) and equation[ii].isdigit():
                    i = equation[ii]
                    num = 10 * num + int(i)
                    ii+=1

                digistack.append(signchange * num)
                ii-=1
            ii+=1

        digi = sum(digistack)
        xd = sum(xstack)
        if xd == 0 and digi == 0:
            return InfiSol
        if xd == 0 and digi != 0:
            return NoSol
        if xd != 0:
            return OneSol + str(- float(digi / xd))

