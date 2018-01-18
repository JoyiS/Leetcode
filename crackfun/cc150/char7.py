# 8.1
def fibn(n):
    if n==1:
        fib = 1
    if n==2:
        fib = 1
    if n>2:
        return fibn(n-2)+fibn(n-1)
    return fib

# 8.2
def ngrid(x,y):
    if x==1 and y==1:
        total = 0
    if x==1 and y>1:
        total = 1
    if y==1 and x>1:
        total = 1
    if x > 1 and y > 1:
        return ngrid(x-1,y)+ngrid(x,y-1)
    return total

#8.3 all sets in a set
def allset(s,n):
    if s==None:
        return None
    if n==0:
        return s
    if n==1:
        return [[s[0]],[s[1]]]
    if n>1:
        return allset(s,n-1) + [a+[s[n]]for a in allset(s, n - 1) + [[]]]

# 8.4 Permutate a string
def permutate(s,n):
    if n==1:
        return s
    if n==2:
        return [s,s[n-1]+s[n-2]]
    if n>2:
        return [sp[0:a]+s[len(sp)]+sp[a:] for sp in permutate(s[:n-1],n-1) for a in range(0,len(sp)+1)]


#8.5
# This problem is important and the tricky part is everytime in the recursive process:
# you should go to one level only (at that level, even you produce two different result,
# they should be in parallel, if the two results generated in one recursive call is not well in parallel,
# it will be wrong and generate repeated results.)
def printpar(l,r,string='',count=0):
    if r<l:
        return None
    if r==0 and l==0:
        print(string)
    if r>l:
        string = string[:count] + ')'
        printpar(l, r - 1, string, count + 1)
    if l>0:
        string =string[:count]+'('
        printpar(l-1,r,string,count+1)



#8.6
def paintfill(xlimit,ylimit, ccscreen,x,y, ocolor, ncolor):
    if x<0 or x>xlimit or y<0 or y>ylimit:
        return False
    if ccscreen[x][y] == ocolor:
        ccscreen[x][y] = ncolor
        paintfill(xlimit, ylimit, ccscreen, x - 1, y, ocolor, ncolor)
        paintfill(xlimit, ylimit, ccscreen, x + 1, y, ocolor, ncolor)
        paintfill(xlimit, ylimit, ccscreen, x, y - 1, ocolor, ncolor)
        paintfill(xlimit, ylimit, ccscreen, x, y + 1, ocolor, ncolor)
    return True

#8.7
# a way to represent n cents
def ncents(value,denom):
    if denom == 25:
        nextdenom = 10
    if denom == 10:
        nextdenom = 5
    if denom == 5:
        nextdenom = 1
    if denom == 1:
        return 1
    ways = 0
    for i in range(0,int(value/denom)+1):
        ways += ncents(value-i*denom, nextdenom)
    return ways

# 8.8 place Queen

colposRow = [0,0,0]

def qrule(colposRow, row):
    for i in range(0,len(colposRow)):
        if row != i and colposRow[row] == colposRow[i]:
            return False
        if row != i and colposRow[row] - colposRow[i] == (row - i):
            return False
    return True

def placeq(row,colposRow):
    if row == 2:
        print(colposRow)
        return True
    for i in range(0, len(colposRow)):
        colposRow[row] = i
        if qrule(colposRow, row):
            placeq(row+1, colposRow)