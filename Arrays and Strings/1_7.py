# Write an algorithm such that if an element in an M*N matrix is 0. Its entire row and column are set to 0
import unittest


def cleanRowsColumns(matrix):
    rows = []
    columns = []
    rows_count = len(matrix)
    assert rows_count != 0
    columns_count = len(matrix[0])
    assert columns_count != 0
    for i in range(rows_count):
        for j in range(columns_count):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)
    for index in range(columns_count):
        for row in rows:
            matrix[row][index] = 0
    for index in range(rows_count):
        for column in columns:
            matrix[index][column] = 0


class Test(unittest.TestCase):
    def testCleaning(self):
        matrix = [[0, 1], [1, 1]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 1]])
        matrix = [[0, 1], [1, 0]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 0]])
        matrix = [[0, 0], [1, 0]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 0]])
        matrix = [[0, 0], [0, 0]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 0]])
        matrix = [[1]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[1]])
        matrix = [[0]]
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0]])
        matrix = [[i for i in range(j, j + 3)] for j in range(4)]
        matrix[1][1] = 0
        cleanRowsColumns(matrix)
        self.assertEqual(matrix, [[0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 5]])