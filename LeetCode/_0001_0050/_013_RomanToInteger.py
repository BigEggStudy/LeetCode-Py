#-----------------------------------------------------------------------------
# Runtime: 56ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def romanToInt(self, s: str) -> int:
        letter_map = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        result = 0
        previous = 0
        for ch in s[::-1]:
            current = letter_map[ch]
            if (current < previous):
                result -= current
            else:
                result += current
            previous = current

        return result
