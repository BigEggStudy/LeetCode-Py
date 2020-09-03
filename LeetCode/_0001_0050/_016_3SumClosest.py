#-----------------------------------------------------------------------------
# Runtime: 92ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()

        result = 0
        difference = 10000
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_value = nums[i] + nums[j] + nums[k]
                new_difference = sum_value - target
                if abs(new_difference) < difference:
                    result = sum_value
                    difference = abs(new_difference)

                if new_difference > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif new_difference < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    return target

        return result
