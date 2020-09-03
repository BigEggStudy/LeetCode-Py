#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def generateParenthesis(self, n: int):
        if n <= 0:
            return ['']
        result = []
        self.__generateParenthesis(n, n, '', result)
        return result

    def __generateParenthesis(self, l: int, r: int, s: str, result):
        if l == 0:
            result.append(s + (')' * r))
            return

        self.__generateParenthesis(l - 1, r, s + '(', result)
        if r > l:
            self.__generateParenthesis(l, r - 1, s + ')', result)
