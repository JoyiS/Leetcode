# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS
    def cloneGraph(self, node):
        if node == None:
            return None
        # original
        queue = []
        queue.append(node)
        # copy
        map = {} # a dict with key = original node, value = copy node
        newhead = UndirectedGraphNode(node.label)
        map[node] = newhead

        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    # make a copy
                    copy = UndirectedGraphNode(neighbor.label)
                    # add copy to the map <original -> copy>
                    map[neighbor] = copy
                    # add graph connections from node to its neighbor
                    map[curr].neighbors.append(copy)
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph???
                    map[curr].neighbors.append(map[neighbor])
        return newhead

# Key points:
'''
(1) queue is used to store the original graph nodes
(2) map is used to store the copy of the graph nodes
'''