#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            nums.reverse()
            return

        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i - 1]:
            j -= 1

        temp = nums[j]
        nums[j] = nums[i - 1]
        nums[i - 1] = temp

        nums[i:] = reversed(nums[i:])
