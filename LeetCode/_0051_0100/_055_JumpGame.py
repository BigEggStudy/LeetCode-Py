#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def canJump(self, nums: [int]) -> bool:
        max_right = 0

        for i, num in enumerate(nums):
            if i > max_right:
                return False
            else:
                max_right = max(max_right, i + num)

        return True
