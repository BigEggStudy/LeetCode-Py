#-----------------------------------------------------------------------------
# Runtime: 44ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queen_column_pos, top_right_diag, top_left_diag):
            row = len(queen_column_pos)
            if row == n:
                return 1

            result = 0
            for col in range(n):
                if col not in queen_column_pos and row + col not in top_right_diag and row - col not in top_left_diag:
                    result += dfs(queen_column_pos + [col], top_right_diag + [row + col], top_left_diag + [row - col])

            return result

        return dfs([], [], [])
