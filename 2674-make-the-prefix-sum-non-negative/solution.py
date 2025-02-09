# Approach: Greedy

# Time: O(n log n)
# Space: O(n)

import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        operations = 0
        prefix_sum = 0
        pq = []

        for num in nums:
            # Push negative numbers to min heap
            if num < 0:
                heapq.heappush(pq, num)

            prefix_sum += num

            # Pop minimum element from heap and subtract from sum
            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(pq)
                operations += 1

        return operations
