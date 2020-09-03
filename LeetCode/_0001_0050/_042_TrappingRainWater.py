#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def trap(self, height: [int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    answer += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    answer += (right_max - height[right])
                right -= 1

        return answer
