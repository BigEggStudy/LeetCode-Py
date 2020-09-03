#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, num in enumerate(nums):
            rest = target - num
            if rest in map:
                return [map[rest], index]
            else:
                map[num] = index

        return []
