#-----------------------------------------------------------------------------
# Runtime: 148ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_length = len(matrix)
        if row_length == 0: return
        col_length = len(matrix[0])

        update_place = []
        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    update_place.append((i,j))

        for row, col in update_place:
            for i in range(row_length):
                matrix[i][col] = 0
            for i in range(col_length):
                matrix[row][i] = 0

    def setZeroes_2(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_length = len(matrix)
        if row_length == 0: return
        col_length = len(matrix[0])

        first_column_zero = False
        first_row_zero = False
        for i in range(row_length):
            if matrix[i][0] == 0:
                first_column_zero = True
                break
        for i in range(col_length):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row_length):
            for j in range(1, col_length):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_column_zero:
            for i in range(row_length):
                matrix[i][0] = 0

        if first_row_zero:
            for i in range(col_length):
                matrix[0][i] = 0
