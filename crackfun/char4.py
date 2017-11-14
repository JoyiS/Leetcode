'''
Tree can be represented/implemented using list or by defining a new class BinaryTree with key, LeftChild and RightChild
'''
from collections import deque

class BTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, leftvalue):
        leftnode = BTreeNode(leftvalue)
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRightChild(self, rightvalue):
        rightnode = BTreeNode(rightvalue)
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self

def getHeight(root):
    if root == None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1

def isBalanced(root):
    if root == None:
        return True
    heightDiff = getHeight(root.left) - getHeight(root.right)
    if abs(heightDiff) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def addtoTree(arr, start, end):
    if end<start:
        return None
    mid = round((start + end)/2)
    btree = BTreeNode(arr[mid])
    btree.left = addtoTree(arr,start,mid-1)
    btree.right = addtoTree(arr,mid+1,end)
    return btree

def printTree(tree):
    if tree != None:
        print(str(tree.value))
        print(str(tree.value) + " left:")
        printTree(tree.left)
        print('~~')
        print(str(tree.value) + " right:")
        printTree(tree.right)

'''
In particular, BFS follows the following steps:

Check the starting node and add its neighbours to the queue.
Get the first node from the queue / remove it from the queue
Mark the starting node as explored.
Check if node has already been visited.
If not, go through the neighbours of the node.
Add the neighbour nodes to the queue.
Mark the node as explored.
Loop through steps 3 to 7 until the queue is empty.
'''

# Traverse a tree
def bfs(graph, start):
    explored = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in explored:
            explored.append(node)
            for neighbor_node in graph[node]:
                if neighbor_node not in explored:
                    queue.append(neighbor_node)
    return explored

def dfs(graph,start):
    explored = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.pop()
        if node not in explored:
            explored.append(node)
            print('explored node: ' + node)
            for neighbor_node in graph[node]:
                if neighbor_node not in explored:
                    queue.append(neighbor_node)
    return explored

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex]:
            if next not in path:
                if next == end:
                    paths.append(path + [next])
                else:
                    queue.append((next, path + [next]))
    return paths




def dfs_paths(graph, start, end):
    queue = [(start,[start])]
    while queue:
        (vertex, path) = queue.pop()
        for next in graph[vertex]:
            if next not in path:
                if next == end:
                    return path + [next]
                else:
                    queue.append((next, path+[next]))
    return paths



'''
question 4.4
'''
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, newn):
        self.next = newn

    def get_data(self):
        return self.data

    def set_data(self, newd):
        self.data = newd


class Linklist(object):
    def __init__(self, r = None):
        self.size = 0
        self.root = r

    def isEmpty(self):
        return self.root == None

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d)
        new_node.set_next(self.root)
        self.root = new_node
        self.size += 1

    def search(self,d):
        Found = False
        current = self.root
        while Found==False:
            if current.get_data() == d:
                Found = True
                return Found
            else:
                current = current.get_next()
        return Found

    def remove(self, d):
        current = self.root
        prev = None
        found = False
        while not found:
            if current.get_data() == d:
                found = True
            else:
                prev = current
                current = current.get_next()

        if prev == None:
            self.root = current.get_next()
        else:
            prev.set_next(current.get_next())
        self.size -= 1

    def insert(self,pos,d):
        if pos == 0:
            self.add(d)
        else:
            current = self.root
            i = 0
            while i < pos - 1:
                i += 1
                current = current.get_next()
            newNode = Node(d)
            newNode.set_next(current.get_next())
            current.set_next(newNode)
        self.size += 1

    def display(self):
        ll = []
        current = self.root
        while current!= None:
            ll.append(current.get_data())
            current = current.get_next()
        return ll


def bstToll(root):
    if root == None:
        return None
    ll = Linklist()
    ll.add(root)
    result = []
    level = 0
    while ll.root is not None:
        level = level + 1
        result.append([level,ll])
        current = ll.root
        ll = Linklist()
        while current is not None:
            if current.data.left is not None:
                ll.add(current.data.left)
            if current.data.right is not None:
                ll.add(current.data.right)
            current = current.get_next()
    return result


def inOrder(root=None, outputs=[]):
  if root is None:
    return None
  inOrder(root.left, outputs)
  outputs.append(root.value)
  inOrder(root.right, outputs)


def findLeftMost(node):
    if node==None:
        return None
    while node.left is not None:
        node = node.left
    return node

def findNextParent(node):
    if node==None:
        return None
    temp = node
    if temp.parent is not None:
        p = temp.parent
    else:
        p = None
    while p and p.left is not temp:
        p = p.parent
        temp = temp.parent
    return p

def next(node):
    if node == None:
        return None
    if node.right is not None:
        findLeftMost(node.right)
    else:
        findNextParent(node)

# Question 4.6 : common ancestor
def common_ancestor(root, node1,node2):
    if node1 == None or node2 == None:
        return None
    if node1==node2 and (root.left == node1 or root.right==node1):
        return root
    if cover(root.left, node1, node2) == 2:
        if root.left == node1 or root.left == node2:
            return root.left
        else:
            return common_ancestor(root.left, node1,node2)
    if cover(root.right,node1,node2) == 2:
        if root.right == node1 or root.right == node2:
            return root.right
        else:
            return common_ancestor(root.right,node1,node2)
    if cover(root.left,node1,node2) == 1:
        return root

# This is key for 4.6
def cover(root, node1, node2):
    ret = 0
    if root == None:
        return ret
    if root == node1 or root == node2:
        ret = ret + 1
    ret = ret + cover(root.left,node1,node2)
    if ret == 2:
        return ret
    return ret+cover(root.right, node1, node2)

# Question 4.7 Subtree
def isSubTree(t1, t2):
  if t2 is None:
    return True

  return hasSubTree(t1, t2)

def hasSubTree(r1, r2):
  if r1 is None:
    return False

  if r1.data == r2.data:
    if isMatchTree(r1, r2):
      return True

  return hasSubTree(r1.left, r2) or hasSubTree(r1.right, r2)

def isMatchTree(r1, r2):
  if r1 is None and r2 is None:
    return True

  if r1 is None or r2 is None:
    return False

  if r1.data == r2.data:
    return isMatchTree(r1.left, r2.left) and isMatchTree(r1.right, r2.right)

  return False

#4.8

if __name__ == "__main__":
    btree = BTreeNode(1)
    btree.setLeftChild(BTreeNode(2))
    btree.setRightChild(BTreeNode(3))
    btree.right.setLeftChild(BTreeNode(4))
    btree.right.left.setLeftChild(BTreeNode(5))
    print(isBalanced(btree))                    # False
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    paths = find_all_paths(graph, 'A','D',path =[])

    arr = [1,2,3,4,5,6,7,8,9]
    btree = addtoTree(arr,0,len(arr)-1)
    printTree(btree)

    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    bfs(graph, 'A')
    dfs(graph, 'A')
    output = bfs_paths(graph, 'A','G')