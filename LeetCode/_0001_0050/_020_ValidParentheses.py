#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for ch in s:
            if ch == ')' or ch == ']' or ch == '}':
                if len(result) == 0:
                    return False
                prev = result.pop()
                if not (ch == ')' and prev == '(') and not (ch == ']' and prev == '[') and not (ch == '}' and prev == '{'):
                    return False
            else:
                result.append(ch)

        return len(result) == 0
