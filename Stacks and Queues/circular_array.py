class CircularArray(object):
    def __init__(self, size):
        # size checking
        if size <= 0:
            raise Exception("Size should be a positive number")
        self._size = size
        self._container = [0] * self._size  # init the container
        self._start = 0  # exit of elements
        self._end = 0  # entrance of elements
        self._addCount = 0
        self._removeCount = 0

    def push(self, value):
        if self.isFull():
            return False
        else:
            self._container[self._end] = value
            self._end = (self._end - 1) % self._size
            self._addCount += 1
            return True

    def pop(self):
        if self.isEmpty():
            return None
        else:
            res = self._container[self._start]
            self._start = (self._start - 1) % self._size
            self._removeCount += 1
            # since remove count must be smaller than add count
            # once they are larger than the size
            # remove the vale of size from both counts in case of overflow
            if self._removeCount > self._size:
                self._removeCount -= self._size
                self._addCount -= self._size
            return res

    def isEmpty(self):
        return self._addCount == self._removeCount

    def isFull(self):
        return self._addCount - self._removeCount == self._size