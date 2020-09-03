#-----------------------------------------------------------------------------
# Runtime: 52ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def combinationSum(self, candidates: [], target: int):
        def dfs(nums, target_rest: int, current_answer: [], results: []):
            if target_rest == 0:
                results.append(list(current_answer))
                return

            for i, num in enumerate(nums):
                if num > target_rest:
                    return

                current_answer.append(num)
                dfs(nums[i:], target_rest - num, current_answer, results)
                current_answer.pop()

        candidates.sort()
        results = []
        dfs(candidates, target, [], results)
        return results
