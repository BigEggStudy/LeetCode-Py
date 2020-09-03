#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0

        row_lenght = len(obstacleGrid)
        column_lenght = len(obstacleGrid[0])

        if row_lenght <= column_lenght:
            possiblePath = [0] * row_lenght
            possiblePath[0] = 1

            for i in range(column_lenght):
                for j in range(row_lenght):
                    possiblePath[j] = 0 if obstacleGrid[j][i] == 1 else (possiblePath[j] if j == 0 else possiblePath[j - 1] + possiblePath[j])

            return possiblePath[-1]
        else:
            possiblePath = [0] * column_lenght
            possiblePath[0] = 1

            for i in range(row_lenght):
                for j in range(column_lenght):
                    possiblePath[j] = 0 if obstacleGrid[i][j] == 1 else (possiblePath[j] if j == 0 else possiblePath[j - 1] + possiblePath[j])

            return possiblePath[-1]
