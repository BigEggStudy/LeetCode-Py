#-----------------------------------------------------------------------------
# Runtime: 56ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        if len(nums) == 1:
            return [ nums ]

        nums.sort()
        visited = [False] * len(nums)
        result = []
        temp_result = []

        def dfs(temp_result: [int]):
            if len(nums) == len(temp_result):
                result.append(temp_result.copy())
                return

            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                temp_result.append(nums[i])
                visited[i] = True
                dfs(temp_result)
                visited[i] = False
                temp_result.pop()

        dfs(temp_result)
        return result
