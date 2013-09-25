from unittest import TestCase
from binTree import BinTree, BinTreeNode

def commonAncenstor(root, node1, node2):
    # calculate both paths
    path1 = []
    findPath(root, node1, path1)
    path2 = []
    findPath(root, node2, path2)
    # compare paths
    index = 0
    result = None
    while index < len(path1) and index < len(path2):
        if path1[index] == path2[index]:
            result = path1[index]
        else:
            break
    return result


def findPath(root, node, storage):
    storage.append(root)
    if root is None:
        storage.pop()
        return False
    elif root != node:
        if findPath(root.left, node, storage) or findPath(root.right, node, storage):
            return True
        else:
            storage.pop()
            return False
    else:
        return True


class TestFindPath(TestCase):
    def testRoot(self):
        tree = BinTree(0)
        storage = []
        findPath(tree.root, tree.root, storage)
        self.assertEqual(storage, [tree.root])

    def testNone(self):
        tree = BinTree(0)
        storage = []
        findPath(tree.root, BinTreeNode(), storage)
        self.assertEqual(storage, [])

    def testUnbalacedTree(self):
        tree = BinTree(0)
        node1 = BinTreeNode()
        node2 = BinTreeNode()
        node3 = BinTreeNode()
        node4 = BinTreeNode()
        tree.root.left = node1
        node1.left = node2
        node2.left = node3
        node3.left = node4
        storage = []
        findPath(tree.root, node4, storage)
        self.assertEqual(storage, [tree.root, node1, node2, node3, node4])

    def testNormalTree(self):
        tree = BinTree(0)
        node1 = BinTreeNode()
        node2 = BinTreeNode()
        node3 = BinTreeNode()
        node4 = BinTreeNode()
        tree.root.left = node1
        tree.root.right = node2
        node1.left = node4
        node2.left = node3
        storage = []
        findPath(tree.root, node3, storage)
        self.assertEqual(storage, [tree.root, node2, node3])
