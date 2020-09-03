#-----------------------------------------------------------------------------
# Runtime: 100ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution(object):
    def findMedianSortedArrays(self, nums1: [], nums2: []):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[length // 2]
        else:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2
