#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys

class Solution:
    def maxArea(self, height) -> int:
        max_area, l, r = 0, 0,  len(height) - 1

        while l < r:
            if height[l] <= height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            if max_area <= area:
                max_area = area
        return max_area
