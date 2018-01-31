def mergesort(s):
    if len(s) > 1:
        m = int(len(s)/2)
        sl = s[:m]
        sr = s[m:]
		mergesort(sl)
		mergesort(sr)
        i=0
        j=0
        k=0

        while i<len(sl) and j<len(sr):
            if sl[i]<sr[j]:
                s[k]=sl[i]
                i+=1
                k+=1
            else:
                s[k]=sr[j]
                j+=1
                k+=1
        while i<len(sl):
            s[k]=sl[i]
            i+=1
            k+=1
        while j<len(sr):
            s[k]=sr[j]
            j+=1
            k+=1

# Quick Sort
def quicksort(s,start,end):
	if start<end:
	    pivot = partition(s,start,end)
		quicksort(s, start, pivot-1)
	    quicksort(s,pivot+1,end)

def partition(s,start,end):
	leftmark=start+1
	rightmark=end
	done = False
	while done is not True:
	    while leftmark<=rightmark and s[leftmark]<=s[start]:
			leftmark+=1
		while rightmark>=leftmark and s[rightmark]>=s[start]:
		    rightmark-=1
		if leftmark > rightmark:
		    done=True
		else:
		    temp = s[leftmark]
			s[leftmark] = s[rightmark]
            s[rightmark] = temp
	temp = s[0]
	s[0]=s[rightmark]
	s[rightmark]=temp
    print('pivot: '+ str(rightmark ))
	return rightmark


def sortColors(nums):
    # quicksort
    def partition(numlist):
        start = 0
        key = numlist[start]
        i = 1
        j = len(numlist) - 1
        done = False
        while not done:
            while i <= j and numlist[i] <= key:
                i += 1
            while j >= i and numlist[j] >= key:
                j -= 1
            if i > j:
                done = True
            else:
                temp = numlist[i]
                numlist[i] = numlist[j]
                numlist[j] = temp
        numlist[0] = numlist[j]
        numlist[j] = key
        return j

    if len(nums) > 1:
        pivot = partition(nums)
        sortColors(nums[:pivot])
        sortColors(nums[pivot + 1:])

    def quickSort(alist):
        quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(alist, first, last):
        if first < last:
            splitpoint = partition(alist, first, last)

            quickSortHelper(alist, first, splitpoint - 1)
            quickSortHelper(alist, splitpoint + 1, last)

    def partition(alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

# insertion sort
def insert(s):
	for i in range(0, len(s)):
		current = s[i]
        j=i
        while j>0 and s[j-1]>current:
            s[j] = s[j-1]
            j-=1
		# for j in range(0,i+1):
		# 	if s[j]>current:
		# 		s[j+1:i+1] = s[j:i]
		# 		s[j] = current
         #        break
        s[j] = current
	return s


# 9.1
def mergeab(a,b,m,n):
    k=m+n-1
    i=m-1
    j=n-1
    while i>=0 and j>=0:
        if a[i]>b[j]:
            a[k]=a[i]
            k-=1
            i-=1
        else:
            a[k]=b[j]
            k-=1
            j-=1
    while i>=0:
        a[k]=a[i]
        k-=1
        i-=1
    while j>=0:
        a[k]=b[j]
        k-=1
        j-=1
    return a

#9.2

def anagram_cluster(lst):
    anagrams = {}
    for elem in lst:
        sig = str(sorted(elem))
        if sig not in anagrams:
            anagrams[sig] = []
        anagrams[sig].append(elem)
    result = []
    for variants in anagrams.values():
        result.extend(variants)
    return result

#9.3 binary search
def bsch(s,l,r,key):
    while l<r:
        m = int((l+r)/2)
        if s[m]==key:
            return m
        elif s[l]<=s[m]:
            if key>s[m]:
                l=m+1
            elif key>=s[l]:
                u=m-1
            else:
                l=m+1
        else:
            if key<=s[m]:
                u = m-1
            elif key>=s[l]:
                u = m-1
            else:
                l = m+1
    return -1

# 9.5
def strsch(s,l,r,key):
    while l<r:
        m=int((l+r)/2)
        while s[m]=='':
            m=m+1
        if s[m]==key:
            return m
        elif s[m]<key:
            l=m+1
            while s[l]=='':
                l=l+1
        else:
            r=m-1
            while s[r]=='':
                r=r-1

    return -1

#9.6
def matrixfind(s,rowe, cole,key):
    row = 0
    col = cole
    while row<rowe and col>=0:
        if s[row][col]==key:
            return row,col
        elif s[row][col]<=key:
            row=row+1
        else:
            col=col-1
    return -1

#9.7
class person(object):
    def __init__(self,h,w):
        self.h=h
        self.w=w

def sortperson(p1,p2):
    if p1.h<p2.h or (p1.h==p2.h and p1.w<=p2.w):
        return True
    return False

def sortplist(p):
    newp = sorted(p,key=lambda x: x.h)
    return newp

if __name__ == '__main__':
    newp= sorplist(p)
    k=1
    d=[]
    d.append(newp[0].w)
    for i in range(1,len(newp)):
        if newp[i].w > d[i-1]:
            k+=1
            d[k]=newp[i].w
        else:
            jj= k-1
            for j in range(k-1,-1,-1):
                if d[j]<p[i].w:
                    break
                else:
                    jj=j-1
            d[jj] = p[i].w
    return k














