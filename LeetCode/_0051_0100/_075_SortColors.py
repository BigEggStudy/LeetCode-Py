#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, lt, gt = 0, 0, len(nums) - 1
        while i <= gt:
            if nums[i] == 0:
                temp = nums[lt]
                nums[lt] = nums[i]
                nums[i] = temp
                lt += 1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[gt]
                nums[gt] = 2
                gt -= 1
            else:
                i += 1
