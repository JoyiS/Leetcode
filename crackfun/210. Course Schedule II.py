class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Construct graph and indegree number:
        graph = [[] for _ in xrange(numCourses)]
        inDegree = [0 for _ in xrange(numCourses)]
        res = []
        cnt = 0
        for x, y in prerequisites:
            graph[y].append(x)
            inDegree[x] += 1
        # Pick all the vertices with indegree = 0 and enque
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        # deque and increment the count of visited node by 1
        # repeat until the queue is empty
        while queue:
            u = queue.pop(0)
            res.append(u)
            for i in graph[u]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)
            cnt += 1

        if cnt == numCourses:
            return res
        else:
            return []

#--------------------------------------
class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.V = []
        self.graph = {}
        for pair in prerequisites:
            if pair[0] not in self.V:
                self.V += [pair[0]]
            if pair[1] not in self.V:
                self.V += [pair[1]]
            self.addEdge(pair[0], pair[1])
        stack = self.topologicalSort()
        if len(stack) == len(self.V):
            for x in range(numCourses):
                if x not in self.V:
                    stack.append(x)
        return stack

    def addEdge(self, u, v):
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v] += [u]

    def topologicalSortUtil(self, x, stack, key):
        self.visited[x] = True
        if x in self.graph:
            for k in self.graph[x]:
                if k in key:
                    self.flag = 1
                    break
                if not self.visited[k]:
                    self.topologicalSortUtil(k, stack, key + [k])
        stack.insert(0, x)

    def topologicalSort(self):
        stack = []
        self.visited = {}
        self.flag = 0
        for x in self.V:
            self.visited[x] = False
        for x in self.V:
            if self.visited[x] == False:
                self.topologicalSortUtil(x, stack, [x])
        if self.flag:
            return []
        return stack