'''
Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.

Time Complexity O((|V|+|E|)log|V|) geeks say O(E+VLogV) (with the use of Fibonacci heap
Space Complexity O(|V|)

下面写的代码中值得注意的是：
1) Graph 用二维matrix来实现，graph[u][v] 表示 u 到 v 的距离。如果 uv 不通， 那么 graph[u][v] = 0
2) dijkstra 的输入是 src 和 des 两个vertex。需要keep一个visited的set来表示这个vertex有没有被访问过。需要一个dist[]来记录每一个vertex的distance.
3) 在dijkstra中每一次循环的第一步是找一个当前没有visited的vertex这个vertex的distance是最小的。然后去更新这个vertex的每一个neighbor的dist [].

'''

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, visited):

        # Initilaize minimum distance for next node
        mindis = float('inf')

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if visited[v] == False and dist[v] < mindis:
                mindis = dist[v]
                min_index = v
        return min_index, mindis


    def dijkstra(self, src, des):

        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V
        output = []

        for x in range(self.V):
            u, mindis = self.minDistance(dist, visited)
            output += [u]
            if u == des:
                print('Min distance is : ' + str(mindis))
                return output
            visited[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]



# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0,8)