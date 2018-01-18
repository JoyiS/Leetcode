class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0] or not B or not B[0]:
            return []
        rowA = len(A)
        rowB = len(B)
        colA = len(A[0])
        colB = len(B[0])
        M = [[0 for j in range(colB)] for i in range(rowA)]
        for i in range(rowA):
            for j in range(colA):
                if A[i][j]:
                    for p in range(colB):
                        M[i][p]+=A[i][j]*B[j][p]
        return M