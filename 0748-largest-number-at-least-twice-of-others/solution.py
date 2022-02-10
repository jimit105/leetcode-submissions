# Time: O(N)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        max1_idx = 0
        
        for i, n in enumerate(nums):
            if n >= max1:
                max2 = max1
                max1 = n
                max1_idx = i
            elif n > max2:
                max2 = n
        
        return max1_idx if max1 >= 2 * max2 else -1
        
