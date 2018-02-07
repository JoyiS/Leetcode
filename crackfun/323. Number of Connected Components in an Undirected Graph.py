'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = {}
        self.V = []
        parent = {}
        res = n
        for edge in edges:
            self.addEdge(edge[0], edge[1])
        for x in range(n):
            self.V.append(x)
            parent[x] = -1

        for i in self.graph:
            for j in self.graph[i]:
                x = self.findparent(parent, i)
                y = self.findparent(parent, j)
                if x != y:
                    self.union(parent, x, y)
                    res -= 1
        return res

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def union(self, parent, x, y):
        x_set = self.findparent(parent, x)
        y_set = self.findparent(parent, y)
        parent[x_set] = y_set

    def findparent(self, parent, x):
        if parent[x] != -1:
            return self.findparent(parent, parent[x])
        return x

