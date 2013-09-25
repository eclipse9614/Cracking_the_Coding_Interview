def isBalancedTree(tree):
    def _getHeight(node):
        if node is None:
            return 0
        else:
            left = _getHeight(node.left)
            right = _getHeight(node.right)
            cur = max(left, right) + 1
            # unbalance checking
            if abs(left - right) > 1 or left == -1 or right == -1:
                cur = -1
            return cur
    if _getHeight(tree.root) != -1:
        return True
    else:
        return False