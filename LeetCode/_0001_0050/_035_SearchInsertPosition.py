#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        return lo
