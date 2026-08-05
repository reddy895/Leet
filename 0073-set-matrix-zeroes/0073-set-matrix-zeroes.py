class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0