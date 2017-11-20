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

