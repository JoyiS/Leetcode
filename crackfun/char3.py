'''
QUEUE: FIFO
STACK: LIFO
'''

class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def deque(self):
        self.items.pop()
        return self.items

    def size(self):
        return len(self.items)

class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:  # This is to delete the last stack if it get empty
            self.stacks.pop()
        return data

    # Pop operation on a specifit sub-stack. (Index begins with 1)
    # Not "rolling over" version. OK with some stacks not at full capacity
    def popAt(self, index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index - 1]) == 0:
            return None
        else:
            return self.stacks[index - 1].pop()
            # -----------------test-------------------


def test():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print(i)

    for i in range(5):
        print("Poped", setofstacks.pop())

    print("Test for popAt")
    for i in range(5):
        for i in range(3):
            print("Poped", setofstacks.popAt(i + 1))

class Hanoi:
    def __init__(self, size):
        self.size = size
        self.rod = [[],[],[]]
        self.disksize = size
        self.rod[0] = [x for x in range(size,0,-1)]

    def display(self):
        print('Rod 1 : ' + str(self.rod[0]) + ' Rod 2 : ' + str(self.rod[1]) + ' Rod 3 : ' + str(self.rod[2]))


    def playHanoi(self):
        print('Game Starts')
        self.movedisk(self.size,1,2,3)
        print('Game Complete, Results:')
        self.display( )

    def movedisk(self,size,fr,temp,to):
        if size == 1:
            data = self.rod[fr-1].pop()
            if data != None:
                self.rod[to-1].append(data)
                print('Disk ' + str(data) + ' is moved from Rod ' + str(fr) + ' --> Rod ' + str(to) +'.')
            else:
                print('Rod : ' + fr + ' is empty')
        else:
            self.movedisk(size-1, fr, to, temp)
            self.movedisk(1, fr, temp, to)
            self.movedisk(size-1, temp, fr, to)

def testHanoi():
    hahanoi = Hanoi(3)
    hahanoi.playHanoi()

#3.6
def sortstack(s):
    r = stack()
    while (s.isEmpty()!= True):
        temp = s.pop()
        while(r.isEmpty()!= True and temp > r.peek()): # the order of these two condition is important
            s.push(r.pop())
        r.push(temp)
    return r

if __name__ == "__main__":
    test()
    testHanoi()
    s = stack()
    s.push(10)
    s.push(5)
    r = sortstack(s)




