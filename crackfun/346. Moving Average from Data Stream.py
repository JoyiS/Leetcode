class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.cap = size
        self.items = []
        self.size = len(self.items)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size==self.cap:
            self.size-=1
            self.items.pop(0)
        self.items.append(val)
        self.size+=1
        return sum(self.items)/self.size


        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)