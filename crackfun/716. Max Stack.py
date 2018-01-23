'''
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
'''

# Straightforward idea with O(n) time and space complexity

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        self.maxstk=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if not self.maxstk:
            self.maxstk.append(x)
        else:
            self.maxstk.append(max(x,self.maxstk[-1]))

    def pop(self):
        """
        :rtype: int
        """
        self.maxstk.pop()
        return self.stk.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxstk[-1]

    def popMax(self):
        """
        :rtype: int
        """
        n=self.maxstk.pop()
        i=len(self.stk)-1
        tmp=[]
        while n!=self.stk[-1]:
            tmp.append(self.pop())
        ret=self.stk.pop()
        for i in range(len(tmp)-1,-1,-1):
            self.push(tmp[i])
        return ret