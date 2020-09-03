#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

INT_MIN = -2 ** 31

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        max_sum = INT_MIN
        curr_max_sum = 0
        for num in nums:
            curr_max_sum = num if curr_max_sum < 0 else curr_max_sum + num
            max_sum = max(max_sum, curr_max_sum)
        return max_sum
