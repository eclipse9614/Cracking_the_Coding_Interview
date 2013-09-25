class BinTree(object):
    def __init__(self, value):
        self._root = BinTreeNode()
        self._root.value = value

    @property
    def root(self):
        return self._root


class BinTreeNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None