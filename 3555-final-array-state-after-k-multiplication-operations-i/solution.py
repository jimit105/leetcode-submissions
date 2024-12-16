# Approach 2: Heap

# Time: O(n + k log n)
# Space: O(n)

import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        pq = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        for _ in range(k):
            _, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))

        return nums
        
