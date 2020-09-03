#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def jump(self, nums: [int]) -> int:
        count = max_right = current_right = 0

        for i, num in enumerate(nums):
            if i > max_right:
                return 0
            if i > current_right:
                current_right = max_right
                count += 1
            if i + num > max_right:
                max_right = i + num

        return count
