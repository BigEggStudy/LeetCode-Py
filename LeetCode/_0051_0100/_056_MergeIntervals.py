#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = []
        for interval in intervals:
            last_interval = result[-1] if len(result) > 0 else None

            if last_interval is not None and last_interval[1] >= interval[0]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                result.append(interval)

        return result
