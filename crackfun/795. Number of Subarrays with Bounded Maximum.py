'''
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
'''

'''
    https://www.geeksforgeeks.org/number-subarrays-maximum-value-given-range/
'''

# Python program to count
# subarrays whose maximum
# elements are in given range.

# function to calculate N*(N+1)/2
def countSubarrys(n):
    return n * (n + 1) // 2

def countSubarrays(a, n, L, R):
    res = 0
    exc = 0
    inc = 0
    for i in range(n):
        print(exc,inc,res)
        if (a[i] > R):
            res = res + (countSubarrys(inc) - countSubarrys(exc))
            inc = 0
            exc = 0
        elif (a[i] < L):
            exc = exc + 1
            inc = inc + 1
        else:
            res = res - countSubarrys(exc)
            exc = 0
            inc = inc + 1
    # Update result.
    res = res + (countSubarrys(inc) - countSubarrys(exc))
    print(res)
    # returns the count of sub-arrays
    return res
