#-----------------------------------------------------------------------------
# Runtime: 24ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        group = 1
        for i in range(1, n + 1):
            nums.append(i)
            group *= i

        if k > group: return ""
        k = k - 1 if k > 0 else 0

        result = ''
        index = -1
        while n > 0:
            group //= n
            index = k // group
            result += str(nums[index])
            nums.remove(nums[index])

            k = k % group
            n -= 1

        return result
