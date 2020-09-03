#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''

        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if len(prefix) == 0:
                return ''
        return prefix
