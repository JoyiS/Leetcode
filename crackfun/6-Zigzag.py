def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2:
        return s
    deltamax = numRows * 2 - 2
    deltastep = list(range(2,deltamax,2))
    deltastep = deltastep[::-1]

    charrows = [''] * numRows
    for i in range(numRows):
        if i == 0 or i == numRows-1:
            j = i
            while j < len(s):
                charrows[i]+=s[j]
                j += deltamax
        else:
            j = i
            step = deltastep[i-1]
            while j < len(s):
                charrows[i] += s[j]
                j += step
                step = deltamax - step

    chaall = ''
    for i in range(numRows):
        if charrows[i]:
            chaall += charrows[i]
    return chaall