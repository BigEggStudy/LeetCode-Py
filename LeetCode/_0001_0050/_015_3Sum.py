#-----------------------------------------------------------------------------
# Runtime: 400ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def threeSum(self, nums: []):
        result = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        nums = sorted(counts)

        for i, num in enumerate(nums):
            if counts[num] >= 2:
                if num == 0:
                    if counts[num] >= 3:
                        result.append([0, 0, 0])
                else:
                    if (-2 * num) in counts:
                        result.append([num, num, -2 * num])

            if num < 0:
                for left in range(i + 1, len(nums)):
                    if nums[left] > - (num + nums[-1]):
                        if (left > i + 1):
                            left -= 1
                        break
                for right in range(left, len(nums)):
                    if nums[right] > (-num // 2):
                        break

                for num2 in nums[left:right]:
                    num3 = - (num + num2)
                    if num3 in counts and num3 != num2:
                        result.append([num, num2, num3])
        return result
