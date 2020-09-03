#-----------------------------------------------------------------------------
# Runtime: 52ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def removeDuplicates(self, nums: []) -> int:
        if len(nums) < 2:
            return len(nums)

        result = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[result] = nums[i]
                result += 1

        return result
