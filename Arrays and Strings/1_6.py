# Given an image represented by an N*N matrix, where each pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degree, Can you do this in place?
import unittest


def _coordinateConverter(size, x, y, left=True):
    if left:
        return size - y - 1, x
    else:
        return y, size - x - 1


def rotateImage(img, left=True):
    size = len(img)
    container = [[0] * size for j in range(size)]
    for i in range(size):
        for j in range(size):
            newX, newY = _coordinateConverter(size, i, j, left)
            container[newX][newY] = img[i][j]
    return container


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def rotateImageInPlace(img, left=True):
    size = len(img)
    for layer in range(size / 2):
        for y in range(layer, size - layer - 1):
            fourCorners = [
                Point(layer, y),  # original
                Point(*_coordinateConverter(size, layer, y)),  # left
                Point(*_coordinateConverter(size, *_coordinateConverter(size, layer, y))),  # left left
                Point(*_coordinateConverter(size, layer, y, False)),  # right
            ]
            backup = img[fourCorners[0].x][fourCorners[0].y]
            if left:
                img[fourCorners[0].x][fourCorners[0].y] = img[fourCorners[3].x][fourCorners[3].y]
                img[fourCorners[3].x][fourCorners[3].y] = img[fourCorners[2].x][fourCorners[2].y]
                img[fourCorners[2].x][fourCorners[2].y] = img[fourCorners[1].x][fourCorners[1].y]
                img[fourCorners[1].x][fourCorners[1].y] = backup

            else:
                img[fourCorners[0].x][fourCorners[0].y] = img[fourCorners[1].x][fourCorners[1].y]
                img[fourCorners[1].x][fourCorners[1].y] = img[fourCorners[2].x][fourCorners[2].y]
                img[fourCorners[2].x][fourCorners[2].y] = img[fourCorners[3].x][fourCorners[3].y]
                img[fourCorners[3].x][fourCorners[3].y] = backup


class Test(unittest.TestCase):
    def testEasyMethod(self):
        # 3 * 3
        matrix = [[i + 1 for i in range(x * 3, (x + 1) * 3)] for x in range(0, 3)]
        leftTurned = [[x, x + 3, x + 6] for x in range(3, 0, -1)]
        rightTurned = [[x + 6, x + 3, x] for x in range(1, 4)]
        self.assertEqual(rotateImage(matrix), leftTurned)
        self.assertEqual(rotateImage(matrix, False), rightTurned)
        # 1 * 1
        self.assertEqual(rotateImage([[1]]), [[1]])
        self.assertEqual(rotateImage([[1]], False), [[1]])
        # 2 * 2
        matrix = [[1, 1], [3, 4]]
        leftTurned = [[1, 4], [1, 3]]
        rightTurned = [[3, 1], [4, 1]]
        self.assertEqual(rotateImage(matrix), leftTurned)
        self.assertEqual(rotateImage(matrix, False), rightTurned)

    def testInPlace(self):
        # 3 * 3
        matrix = [[i + 1 for i in range(x * 3, (x + 1) * 3)] for x in range(0, 3)]
        leftTurned = [[x, x + 3, x + 6] for x in range(3, 0, -1)]
        rotateImageInPlace(matrix)
        self.assertEqual(matrix, leftTurned)
        # two right turns will direct it to the right
        rotateImageInPlace(matrix, False)
        rotateImageInPlace(matrix, False)
        rightTurned = [[x + 6, x + 3, x] for x in range(1, 4)]
        self.assertEqual(matrix, rightTurned)
        # 1 * 1
        matrix = [[1]]
        rotateImageInPlace(matrix)
        self.assertEqual(matrix, [[1]])
        # two right turns will direct it to the right
        rotateImageInPlace(matrix, False)
        rotateImageInPlace(matrix, False)
        self.assertEqual(matrix, [[1]])
        # 2 * 2
        matrix = [[1, 1], [3, 4]]
        leftTurned = [[1, 4], [1, 3]]
        rightTurned = [[3, 1], [4, 1]]
        rotateImageInPlace(matrix)
        self.assertEqual(matrix, leftTurned)
        rotateImageInPlace(matrix, False)
        rotateImageInPlace(matrix, False)
        self.assertEqual(matrix, rightTurned)
        # 4 * 4
        matrix = [[i + 1 for i in range(x * 4, (x + 1) * 4)] for x in range(0, 4)]
        leftTurned = [[x, x + 4, x + 8, x + 12] for x in range(4, 0, -1)]
        rotateImageInPlace(matrix)
        self.assertEqual(matrix, leftTurned)