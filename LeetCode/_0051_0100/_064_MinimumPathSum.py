#-----------------------------------------------------------------------------
# Runtime: 100ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        row_length = len(grid)
        if row_length < 1: return 0
        col_length = len(grid[0])

        for i in range(1, row_length):
            grid[i][0] += grid[i-1][0]
        for j in range(1, col_length):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row_length):
            for j in range(1, col_length):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[-1][-1]
