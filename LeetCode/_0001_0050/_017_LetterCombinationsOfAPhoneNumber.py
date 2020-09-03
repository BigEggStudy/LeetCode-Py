#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import queue

class Solution:
    PHONE_CHARS = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

    def letterCombinations(self, digits: str):
        if len(digits) == 0 or '1' in digits or '0' in digits:
            return []

        result = ['']
        for i in range(len(digits)):
            result = [prev + new_ch for prev in result for new_ch in self.PHONE_CHARS[digits[i]]]

        return result
