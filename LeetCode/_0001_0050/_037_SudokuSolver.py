#-----------------------------------------------------------------------------
# Runtime: 44ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        digits = { str(i) for i in range(1, 10) }
        rows = [ digits.copy() for _ in range(9) ]
        cols = [ digits.copy() for _ in range(9) ]
        boxs = [ [ digits.copy() for _ in range(3) ] for _ in range(3) ]
        unoccupied = set()

        def __recursiveSolver():
            if not unoccupied:
                return

            choices = digits.copy()
            for row, col in unoccupied:
                possible_moves = rows[row] & cols[col] & boxs[row // 3][col // 3]
                if len(possible_moves) < len(choices):
                    action_pos = (row, col)
                    choices = possible_moves
                if len(choices) == 1:
                    break

            for choice in choices:
                (row, col) = action_pos

                unoccupied.remove(action_pos)
                board[row][col] = choice
                rows[row].remove(choice)
                cols[col].remove(choice)
                boxs[row // 3][col // 3].remove(choice)

                __recursiveSolver()
                if not unoccupied: return

                unoccupied.add(action_pos)
                board[row][col] = '.'
                rows[row].add(choice)
                cols[col].add(choice)
                boxs[row // 3][col // 3].add(choice)

        for row in range(9):
            for col in range(9):
                ch = board[row][col]
                if ch == '.':
                    unoccupied.add((row, col))
                else:
                    rows[row].remove(ch)
                    cols[col].remove(ch)
                    boxs[row // 3][col // 3].remove(ch)

        __recursiveSolver()
