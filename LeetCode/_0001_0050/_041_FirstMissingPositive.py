#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def firstMissingPositive(self, nums: []) -> int:
        nums_length = len(nums)
        for i in range(nums_length):
            if nums[i] <= 0:
                nums[i] = nums_length + 1

        for num in nums:
            abs_num = abs(num)
            if abs_num <= nums_length and nums[abs_num - 1] > 0:
                nums[abs_num - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return nums_length + 1
