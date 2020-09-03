#-----------------------------------------------------------------------------
# Runtime: 44ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        if len(nums) == 1:
            return [ nums ]

        result = []
        sub_permutations = self.permute(nums[1:])
        for sub_permutation in sub_permutations:
            for i in range(len(sub_permutation) + 1):
                result.append(sub_permutation[:i] + [ nums[0] ] + sub_permutation[i:])

        return result
