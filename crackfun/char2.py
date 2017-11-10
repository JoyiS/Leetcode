'''
Linked list has the advantages of:
const time concatenation

To define a linked list:
(1) define the node
(2) define the linked-list
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
        self.size +=1

    def display(self):
        ll = []
        current = self.root
        while current!= None:
            ll.append(current.get_data())
            current = current.get_next()
        return ll

myll = Linklist()
myll.add(5)

# Question 2.1
# The key is to guarantee there is no duplicates before this current node
# the action of removing requires a current node and a prev node (two pointer for sure)
# to check the nodes before the current, a runner pointer is required.
def deldups(myll):
    prev = myll.root
    current = prev.get_next()
    while current != None:
        runner = myll.root
        while runner != current:
            if runner.data == current.data:
               temp = current.get_next()
               prev.next = temp
               current = temp
               myll.size -= 1
               break;
            else:
                runner = runner.get_next()
        if runner == current: # This is the line I forgot
            current = current.get_next()
            prev = prev.get_next()

#Question 2.2
def findntoend(myll,n):
    prev = myll.root
    runner = myll.root
    i = 0
    while i<n and runner != None:
        runner = runner.get_next()
        i = i+1
    while runner != None:
        prev = prev.get_next()
        runner = runner.get_next()
    return prev.data

#Question 2.3
# delete a node only accessing this node, node has two attributes, make this node the next node.

#Question 2.4
# >= 10 not > 10
def addtwolist(l1,l2):
    lsum = Linklist()
    currentl1 = l1.root
    currentl2 = l2.root
    more = 0
    size = 0
    while (currentl1 !=None or currentl2 !=None):
        if (currentl1 !=None and currentl2 !=None):
            ll12 = currentl1.data + currentl2.data
            llsum = ll12 % 10 + more
            more = int(ll12 >= 10)
            lsum.insert(size,llsum)
            size += 1
        elif currentl1 !=None:
            ll12 = currentl1.data
            llsum = ll12 % 10 + more
            more = int(ll12>=10)
            lsum.insert(size, llsum)
            size += 1
        else:
            ll12 = currentl2.data
            llsum = ll12 % 10 + more
            more = int(ll12 >= 10)
            lsum.insert(size, llsum)
            size += 1

        currentl1 = currentl1.get_next()
        currentl2 = currentl2.get_next()
    if more ==1:
        lsum.insert(size,more)
    return lsum

