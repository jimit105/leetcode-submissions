# Approach 3: Reservoir Sampling

# Time: O(1) for pick(), O(n) for constructor
# Space: O(n)

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.indices = {} # Dictionary to store number -> list of indices
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)
        

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        return indices[random.randint(0, len(indices) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
