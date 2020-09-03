#-----------------------------------------------------------------------------
# Runtime: 60ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        results = []

        def dfs(queen_column_pos, top_right_diag, top_left_diag):
            row = len(queen_column_pos)
            if row == n:
                results.append(queen_column_pos)
                return

            for col in range(n):
                if col not in queen_column_pos and row + col not in top_right_diag and row - col not in top_left_diag:
                    dfs(queen_column_pos + [col], top_right_diag + [row + col], top_left_diag + [row - col])

        dfs([], [], [])
        return [['.' * queen_col + 'Q' + '.' * (n - 1 - queen_col)  for queen_col in result] for result in results]
