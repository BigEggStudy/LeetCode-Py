#-----------------------------------------------------------------------------
# Runtime: 48ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def combinationSum2(self, candidates: [], target: int):
        def dfs(nums, target_rest: int, current_answer: [], results: []):
            if target_rest == 0:
                results.append(list(current_answer))
                return

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if num > target_rest:
                    return

                current_answer.append(num)
                dfs(nums[i + 1:], target_rest - num, current_answer, results)
                current_answer.pop()

        candidates.sort()
        results = []
        dfs(candidates, target, [], results)
        return results
