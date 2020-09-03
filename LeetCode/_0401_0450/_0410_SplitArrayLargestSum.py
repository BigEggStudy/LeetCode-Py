#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def splitArray(self, nums: [int], m: int) -> int:
        lo, hi = max(nums), sum(nums)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            count, currentSum = 1, 0
            for num in nums:
                currentSum += num
                if currentSum > mid:
                    count += 1
                    if count > m:
                        break
                    currentSum = num
            if count <= m:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
