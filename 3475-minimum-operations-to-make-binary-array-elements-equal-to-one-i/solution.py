# Approach 1: Deque

# Time: O(n)
# Space: O(n)

from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip_queue = deque()
        count = 0

        for i in range(len(nums)):
            # Remove flips older than 3 indices
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()

            if (nums[i] + len(flip_queue)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)

        return count
        
