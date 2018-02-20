class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        graph = [[1 for j in range(N)] for i in range(N)]
        if mines:
            for pos in mines:
                graph[pos[0]][pos[1]] = 0
        else:
            return (N + 1) // 2
        res = 0
        L = [[0 for j in range(N)] for i in range(N)]
        R = [[0 for j in range(N)] for i in range(N)]
        U = [[0 for j in range(N)] for i in range(N)]
        D = [[0 for j in range(N)] for i in range(N)]

        for i in range(N):
            L[i][0] = 1 if graph[i][0] else 0
            for j in range(1, N):
                if graph[i][j] == 1:
                    L[i][j] = L[i][j - 1] + 1
                else:
                    L[i][j] = 0
        for i in range(N):
            R[i][N - 1] = 1 if graph[i][N - 1] else 0
            for j in range(N - 2, -1, -1):
                if graph[i][j] == 1:
                    R[i][j] = R[i][j + 1] + 1
                else:
                    R[i][j] = 0
        for j in range(N):
            U[j][0] = 1 if graph[j][0] else 0
            for i in range(1, N):
                if graph[i][j] == 1:
                    U[i][j] = U[i - 1][j] + 1
                else:
                    U[i][j] = 0
        for j in range(N):
            D[N-1][j] = 1 if graph[N-1][j] else 0
            for i in range(N - 2, -1, -1):
                if graph[i][j] == 1:
                    D[i][j] = D[i + 1][j] + 1
                else:
                    D[i][j] = 0
        for i in range(N):
            for j in range(N):
                if L[i][j] and R[i][j] and U[i][j] and D[i][j]:
                    xx = min([L[i][j] , R[i][j] , U[i][j] , D[i][j]])
                    res = max(res, xx)
        return res



