#-----------------------------------------------------------------------------
# Runtime: 72ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        map = {}
        maxLen = 0
        lastRepeatPos = -1
        for index, char in enumerate(s):
            if char in map and lastRepeatPos < map[char]:
                lastRepeatPos = map[char]
            if maxLen < index - lastRepeatPos:
                maxLen = index - lastRepeatPos
            map[char] = index

        return maxLen
