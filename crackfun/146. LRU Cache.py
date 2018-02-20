from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest
            k, v = self.array.iteritems().next()
            del self.array[k]
        self.array[key] = value



        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


        # 2/4/2018 Python 3 version, iteritems cannot be used

        from collections import OrderedDict

        class LRUCache(object):
            def __init__(self, capacity):
                self.array = OrderedDict()
                self.capacity = capacity

            def get(self, key):
                if key in self.array:
                    value = self.array[key]
                    # Remove first
                    del self.array[key]
                    # Add back in
                    self.array[key] = value
                    return value
                else:
                    return -1

            def put(self, key, value):
                if key in self.array:
                    # Delete existing key before refreshing it
                    del self.array[key]
                elif len(self.array) >= self.capacity:
                    # Delete oldest
                    oldkey = self.array.keys().__iter__().__next__()
                    del self.array[oldkey]
                self.array[key] = value



                # Your LRUCache object will be instantiated and called as such:
                # obj = LRUCache(capacity)
                # param_1 = obj.get(key)
                # obj.put(key,value)


                class LRUCache:

                    def __init__(self, capacity):
                        self.dic = collections.OrderedDict()
                        self.remain = capacity

                    def get(self, key):
                        if key not in self.dic:
                            return -1
                        v = self.dic.pop(key)
                        self.dic[key] = v  # set key as the newest one
                        return v

                    def put(self, key, value):
                        if key in self.dic:
                            self.dic.pop(key)
                        else:
                            if self.remain > 0:
                                self.remain -= 1
                            else:  # self.dic is full
                                self.dic.popitem(last=False)
                        self.dic[key] = value



                        # Your LRUCache object will be instantiated and called as such:
                        # obj = LRUCache(capacity)
                        # param_1 = obj.get(key)
                        # obj.put(key,value)