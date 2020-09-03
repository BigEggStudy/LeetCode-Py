#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)

        if len_needle == 0:
            return 0
        if len_needle > len_haystack:
            return -1

        for i in range(len_haystack):
            if i + len_needle <= len_haystack and needle == haystack[i:i + len_needle]:
                return i
        return -1
