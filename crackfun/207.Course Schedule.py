# This is about topological sort and cyclic graph
# Please check here for more details:
# http://www.geeksforgeeks.org/topological-sorting/
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# 2/6/2018
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for pair in prerequisites:
            if pair[1] not in graph:
                graph[pair[1]] = [pair[0]]
            else:
                graph[pair[1]] += [pair[0]]

        def topologicalSortUtil(i, visited, graph, key):
            visited[i] = True
            if i in graph:
                for x in graph[i]:
                    if x in key:
                        self.flag = 1
                        break
                    if not visited[x]:
                        topologicalSortUtil(x, visited, graph, key + [x])

        def topologicalSort(graph, numCourses):
            visited = [False] * numCourses
            for i in range(numCourses):
                if not visited[i]:
                    topologicalSortUtil(i, visited, graph, [i])
                if self.flag:
                    return
            return

        self.flag = 0
        topologicalSort(graph, numCourses)
        if self.flag:
            return False
        return True

