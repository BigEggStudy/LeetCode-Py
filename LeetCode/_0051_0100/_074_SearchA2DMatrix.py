#-----------------------------------------------------------------------------
# Runtime: 76ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        row_length = len(matrix)
        if row_length == 0:
            return False

        i, j = 0, len(matrix[0]) - 1
        while i < row_length and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False
