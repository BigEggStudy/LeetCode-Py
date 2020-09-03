#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0

        result = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[result] = nums[i]
                result += 1

        return result
