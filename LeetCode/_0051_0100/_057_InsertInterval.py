#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        result = []

        for i, interval in enumerate(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            if end < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < start:
                result.append(newInterval)
                for j in range(i, len(intervals)):
                    result.append(intervals[j])
                return result
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        result.append(newInterval)
        return result
