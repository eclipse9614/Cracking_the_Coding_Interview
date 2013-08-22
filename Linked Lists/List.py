class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class ListIterator(object):
    def __init__(self, head):
        self.current = head

    def next(self):
        if self.current.next:
            self.current = self.current.next
            return self.current.value
        else:
            raise StopIteration()


class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.last = self.head

    def _findNodeBeforePos(self, pos):
        preview = self.head
        for i in range(pos):
            preview = preview.next
            if preview is None:
                raise IndexError()
        return preview

    def append(self, value):
        self.last.next = Node(value)
        self.last = self.last.next

    def insert(self, pos, val):
        # find the node before the pos to be inserted
        preview = self._findNodeBeforePos(pos)
        newNode = Node(val)
        newNode.next = preview.next
        preview.next = newNode
        # update last pointer
        if newNode.next is None:
            self.last = newNode

    def get(self, pos):
        # find the pos
        preview = self._findNodeBeforePos(pos)
        if preview.next:
            return preview.next
        else:
            raise IndexError()

    def delete(self, pos):
        # find the node before the node to be deleted
        preview = self._findNodeBeforePos(pos)
        # delete
        if preview.next:  # if next exist
            preview.next = preview.next.next
        else:
            raise IndexError()

    def __iter__(self):
        return ListIterator(self.head)