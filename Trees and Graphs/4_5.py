def isBinSearchTree(tree):
    def _checkNode(node, lowerLimit, higherLimit):
        if node is None:
            return True
        if lowerLimit is not None and node.value <= lowerLimit:
            return False
        if higherLimit is not None and node.value > higherLimit:
            return False
        return _checkNode(node.left, lowerLimit, node.value) and \
               _checkNode(node.right, node.value, higherLimit)
    return _checkNode(tree.root, None, None)