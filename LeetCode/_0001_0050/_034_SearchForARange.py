#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def __binary_search(self, nums, target, left: bool = False):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums: list, target: int):
        left = self.__binary_search(nums, target, True)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.__binary_search(nums, target) - 1
        return [left, right]
