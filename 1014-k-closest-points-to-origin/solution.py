# Approach 2: Max Heap

# Time: O(n * log k)
# Space: O(k)

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]


    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2
        
