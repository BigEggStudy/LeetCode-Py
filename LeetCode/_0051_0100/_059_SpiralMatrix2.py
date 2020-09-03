#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        total_count = n * n
        current_num = 1
        result = [[0] * n for _ in range(n)]

        level = 0
        while True:
            first_row = level
            first_col = level
            last_row = n - level - 1
            last_col = n - level - 1

            for i in range(first_col, last_col + 1):
                result[first_row][i] = current_num
                current_num += 1
            if current_num > total_count:
                break

            for i in range(first_row + 1, last_row):
                result[i][last_col] = current_num
                current_num += 1
            if current_num > total_count:
                break

            for i in range(last_col, first_col - 1, -1):
                result[last_row][i] = current_num
                current_num += 1
            if current_num > total_count:
                break

            for i in range(last_row - 1, first_row, -1):
                result[i][first_col] = current_num
                current_num += 1
            if current_num > total_count:
                break

            level += 1

        return result
