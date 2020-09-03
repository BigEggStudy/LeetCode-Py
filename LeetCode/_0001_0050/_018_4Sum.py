#-----------------------------------------------------------------------------
# Runtime: 64ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4:
            return []

        nums.sort()
        if (sum(nums[:4], 0) > target or sum(nums[-4:], 0) < target):
            return []

        two_sum = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_value = nums[i] + nums[j]
                if sum_value not in two_sum:
                    two_sum[sum_value] = []
                two_sum[sum_value].append(i)
                two_sum[sum_value].append(j)

        result = []
        for key, index_list1 in two_sum.items():
            if target - key not in two_sum:
                continue

            index_list2 = two_sum[target - key]
            i = 0
            while i < len(index_list1):
                j = 0
                while j < len(index_list2):
                    if index_list1[i + 1] < index_list2[j] and (index_list1[i] != index_list2[j] and index_list1[i] != index_list2[j + 1]):
                        result.append([ nums[index_list1[i]], nums[index_list1[i + 1]], nums[index_list2[j]], nums[index_list2[j + 1]] ])

                        while j + 2 < len(index_list2) and nums[index_list2[j]] == nums[index_list2[j + 2]]:
                            j += 2
                    j += 2
                while i + 2 < len(index_list1) and nums[index_list1[i]] == nums[index_list1[i + 2]]:
                    i += 2
                i += 2

        return result
