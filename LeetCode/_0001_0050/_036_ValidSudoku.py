#-----------------------------------------------------------------------------
# Runtime: 44ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import copy

class Solution:
    def isValidSudoku(self, board) -> bool:
        colUsed = [[False for x in range(9)] for y in range(9)]
        rowUsed = [[False for x in range(9)] for y in range(9)]
        squareUsed = [[False for x in range(9)] for y in range(9)]

        for row in range(9):
            for column in range(9):
                if not board[row][column].isdigit():
                    continue
                squareId = (row // 3) * 3 + column // 3

                value = int(board[row][column]) - 1
                if colUsed[column][value] or rowUsed[row][value] or squareUsed[squareId][value]:
                    return False
                colUsed[column][value] = True
                rowUsed[row][value] = True
                squareUsed[squareId][value] = True

        return True
