#-----------------------------------------------------------------------------
# Runtime: 48ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0

        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, right * 2)
            elif right > left:
                left = right = 0

        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left * 2)
            elif left > right:
                left = right = 0

        return max_length
