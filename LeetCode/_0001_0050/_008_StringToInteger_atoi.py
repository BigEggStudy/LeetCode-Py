#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1
SIGNS = ['+', '-']

class Solution:
    def myAtoi(self, input_string: str) -> int:
        for start_index, char in enumerate(input_string):
            if char != ' ':
                break
        else:
            return 0
        if not char.isnumeric() and not char in SIGNS:
            return 0

        sign = 1
        if char in SIGNS:
            sign = 1 if char == '+' else -1
            start_index = start_index + 1
        if start_index == len(input_string):
            return 0

        result = 0
        for j in range(start_index, len(input_string)):
            char = input_string[j]
            if not char.isnumeric():
                break
            result = result * 10 + int(char)
            if (result > INT_MAX):
                return INT_MAX if sign > 0 else INT_MIN

        return sign * result
