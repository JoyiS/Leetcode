'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
'''


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or not matrix[0]:
            return []

        n = len(matrix[0])
        up = 1
        down = 0
        i = 0
        while matrix and matrix[0]:
            if up:
                while i >= 0:
                    res += [matrix[i].pop(0)]
                    i -= 1
                if not matrix[0]:
                    matrix.pop(0)
                up = 0
                down = 1
                i = 0
                continue
            if down:
                j = min(n + 1 - len(matrix[0]), len(matrix))
                while i < j:
                    res += [matrix[i].pop(0)]
                    i += 1
                if not matrix[0]:
                    matrix.pop(0)
                    i -= 1
                if i >= len(matrix):
                    i = len(matrix) - 1
                up = 1
                down = 0
                continue
        return res

