def nextNodeInOrder(node):
    # no next node for None
    if node is None:
        return None
    # if the right child does exist, the next node would be the most left node for the subtree
    if node.right:
        nextNode = node.right
        while nextNode.left:
            nextNode = nextNode.left
    else:
        # go up until find the parent whose has right child unexploded
        nextNode = None
        while node.parent:
            if node.parent.right == node:
                node = node.parent
            else:
                nextNode = node.parent
                break
    return nextNode