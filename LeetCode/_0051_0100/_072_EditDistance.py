#-----------------------------------------------------------------------------
# Runtime: 128ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length, word2_length = len(word1), len(word2)
        if word1_length == 0: return word2_length
        if word2_length == 0: return word1_length
        if word1_length < word2_length:
            return self.minDistance(word2, word1)

        dp = list(range(word2_length + 1))

        for i in range(1, word1_length + 1):
            upper_left = dp[0]
            dp[0] = i
            for j in range(1, word2_length + 1):
                upper = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = upper_left
                else:
                    left = dp[j-1]
                    dp[j] = min(upper_left, upper, left) + 1
                upper_left = upper

        return dp[-1]
