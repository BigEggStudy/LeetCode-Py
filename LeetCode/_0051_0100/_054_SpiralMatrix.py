#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        row_length = len(matrix)
        if row_length <= 0:
            return matrix
        col_length = len(matrix[0])
        matrix_length = col_length * row_length

        result = []
        level = 0

        while True:
            first_col = level
            first_row = level
            last_col = col_length - level - 1
            last_row = row_length - level - 1

            for i in range(first_col, last_col + 1):
                result.append(matrix[first_row][i])
            if len(result) == matrix_length: break

            for i in range(first_row + 1, last_row):
                result.append(matrix[i][last_col])
            if len(result) == matrix_length: break

            for i in range(last_col, first_col - 1, -1):
                result.append(matrix[last_row][i])
            if len(result) == matrix_length: break

            for i in range(last_row - 1, first_row, -1):
                result.append(matrix[i][first_col])
            if len(result) == matrix_length: break

            level += 1

        return result
