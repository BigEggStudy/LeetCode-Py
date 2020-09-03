#-----------------------------------------------------------------------------
# Runtime: 724ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import collections

class Solution:
    def assignBikes(self, workers: [[int]], bikes: [[int]]) -> [int]:
        distances = collections.defaultdict(list)
        for i, (worker_x, worker_y) in enumerate(workers):
            for j, (bike_x, bike_y) in enumerate(bikes):
                distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                distances[distance].append((i, j))

        usedBike = set()
        result = [ -1 ] * len(workers)
        for key in sorted(distances.keys()):
            for worker_id, bike_id in distances[key]:
                if result[worker_id] == -1 and bike_id not in usedBike:
                    result[worker_id] = bike_id
                    usedBike.add(bike_id)
        return result
