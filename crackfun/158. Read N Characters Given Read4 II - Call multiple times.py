'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        # using a queue data structure is a key to the problem
        self.queue = []
    def read(self, buf, n):
        read, need, buf4 = 0, n, ['']*4
        while need > 0:
            k = read4(buf4)
            self.queue.extend(buf4[:k])
            # This need is the key
            need = min(len(self.queue), n - read)
            buf[read:read+need] = [self.queue.pop(0) for _ in range(need)]
            read += need
        return read