#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def search(self, nums: list, target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[lo] > nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[hi] < nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
